#!/usr/bin/env python3
"""Numerically verify the binding sigma/gamma convention dictionary."""

from __future__ import annotations

import sys

import numpy as np


def block(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    return np.block([[a, b], [c, d]])


def require_close(name: str, actual: np.ndarray, expected: np.ndarray) -> None:
    if not np.allclose(actual, expected):
        print(f"FAIL: {name}")
        print("actual:")
        print(actual)
        print("expected:")
        print(expected)
        raise AssertionError(name)
    print(f"OK: {name}")


def left_grassmann_derivative(
    polynomial: dict[int, int], variable: int
) -> dict[int, int]:
    """Differentiate an exterior polynomial in canonical variable order."""
    result: dict[int, int] = {}
    bit = 1 << variable
    for mask, coefficient in polynomial.items():
        if not mask & bit:
            continue
        variables_to_left = (mask & (bit - 1)).bit_count()
        sign = -1 if variables_to_left % 2 else 1
        new_mask = mask ^ bit
        result[new_mask] = result.get(new_mask, 0) + sign * coefficient
    return result


def scale_polynomial(
    polynomial: dict[int, int], coefficient: int
) -> dict[int, int]:
    return {
        mask: coefficient * value
        for mask, value in polynomial.items()
        if coefficient * value
    }


def main() -> int:
    one = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    sigma = (one, *pauli)
    barsigma = (one, *(-matrix for matrix in pauli))
    eta = np.diag([-1, 1, 1, 1]).astype(complex)

    for mu in range(4):
        for nu in range(4):
            expected = -2 * eta[mu, nu] * one
            require_close(
                f"sigma identity ({mu},{nu})",
                sigma[mu] @ barsigma[nu] + sigma[nu] @ barsigma[mu],
                expected,
            )
            require_close(
                f"barsigma identity ({mu},{nu})",
                barsigma[mu] @ sigma[nu] + barsigma[nu] @ sigma[mu],
                expected,
            )

    gamma = tuple(
        -1j * block(zero, sigma[mu], barsigma[mu], zero)
        for mu in range(4)
    )
    four = np.eye(4, dtype=complex)
    for mu in range(4):
        for nu in range(4):
            require_close(
                f"Clifford identity ({mu},{nu})",
                gamma[mu] @ gamma[nu] + gamma[nu] @ gamma[mu],
                2 * eta[mu, nu] * four,
            )

    gamma5 = -1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    require_close(
        "gamma5 comparison",
        gamma5,
        np.diag([1, 1, -1, -1]).astype(complex),
    )
    beta = 1j * gamma[0]
    require_close("beta comparison", beta, block(zero, one, one, zero))
    require_close(
        "parity block comparison",
        1j * beta,
        block(zero, 1j * one, 1j * one, zero),
    )

    epsilon = np.array([[0, 1], [-1, 0]], dtype=complex)
    require_close("epsilon square", epsilon @ epsilon, -one)
    weinberg_weyl_column = np.array([2 + 3j, -5 + 7j], dtype=complex)
    dotted_lower = epsilon @ weinberg_weyl_column
    require_close(
        "Chapter 25 dotted-index bridge",
        -epsilon @ dotted_lower,
        weinberg_weyl_column,
    )

    # A Majorana row in the comparison dictionary is
    # (x^T epsilon, -y^T epsilon).  These checks compare the coefficient
    # blocks obtained after multiplying by the gamma matrices.
    majorana_bar_map = block(epsilon, zero, zero, -epsilon)
    require_close(
        "scalar bilinear coefficient map",
        majorana_bar_map,
        block(epsilon, zero, zero, -epsilon),
    )
    require_close(
        "pseudoscalar bilinear coefficient map",
        majorana_bar_map @ gamma5,
        block(epsilon, zero, zero, epsilon),
    )
    for mu in range(4):
        require_close(
            f"vector bilinear coefficient map ({mu})",
            majorana_bar_map @ gamma[mu],
            -1j
            * block(
                zero,
                epsilon @ sigma[mu],
                -epsilon @ barsigma[mu],
                zero,
            ),
        )
        require_close(
            f"axial bilinear coefficient map ({mu})",
            majorana_bar_map @ gamma5 @ gamma[mu],
            -1j
            * block(
                zero,
                epsilon @ sigma[mu],
                epsilon @ barsigma[mu],
                zero,
            ),
        )

    for mu in range(4):
        for nu in range(4):
            sigma_mn = (
                sigma[mu] @ barsigma[nu]
                - sigma[nu] @ barsigma[mu]
            ) / 4
            barsigma_mn = (
                barsigma[mu] @ sigma[nu]
                - barsigma[nu] @ sigma[mu]
            ) / 4
            require_close(
                f"tensor block dictionary ({mu},{nu})",
                gamma[mu] @ gamma[nu] - gamma[nu] @ gamma[mu],
                -4 * block(sigma_mn, zero, zero, barsigma_mn),
            )

    # Variable order is theta^1, theta^2, bartheta^dot1, bartheta^dot2.
    theta_squared = {0b0011: 2}
    bartheta_squared = {0b1100: -2}

    def d_squared(polynomial: dict[int, int]) -> dict[int, int]:
        differentiated = left_grassmann_derivative(polynomial, 1)
        differentiated = scale_polynomial(differentiated, -1)
        differentiated = left_grassmann_derivative(differentiated, 0)
        differentiated = scale_polynomial(differentiated, -1)
        return scale_polynomial(differentiated, 2)

    def bard_squared(polynomial: dict[int, int]) -> dict[int, int]:
        differentiated = left_grassmann_derivative(polynomial, 3)
        differentiated = left_grassmann_derivative(differentiated, 2)
        return scale_polynomial(differentiated, -2)

    if d_squared(theta_squared) != {0: -4}:
        raise AssertionError("D^2 theta^2")
    print("OK: D^2 theta^2 = -4")
    if bard_squared(bartheta_squared) != {0: -4}:
        raise AssertionError("bar D^2 bar theta^2")
    print("OK: bar D^2 bar theta^2 = -4")

    highest_monomial = {0b1111: -4}
    projected = bard_squared(highest_monomial)
    # h=theta^2 bartheta^2 has D component 2, while its projected
    # F component is -4: [bar D^2 h]_F=-2[h]_D.
    if projected != {0b0011: -8}:
        raise AssertionError("bar D^2 projection")
    print("OK: [bar D^2 h]_F = -2 [h]_D")

    # bartheta^2 and theta^2 are conjugate ordered monomials.  The two
    # preceding component checks therefore also verify the plus sign in
    # (bar D^2 S)^*=D^2 S^* for this sign-sensitive basis element.
    if bard_squared(bartheta_squared) != d_squared(theta_squared):
        raise AssertionError("squared-superderivative conjugation")
    print("OK: squared-superderivative conjugation")

    print("All binding two-component convention checks passed.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError:
        sys.exit(1)
