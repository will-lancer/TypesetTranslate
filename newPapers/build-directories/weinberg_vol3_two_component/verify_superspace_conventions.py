#!/usr/bin/env python3
"""Verify the edition's ordered two-component superspace conventions.

The calculation uses a four-generator exterior algebra for
theta^1, theta^2, bar-theta^dot1, and bar-theta^dot2.  Spacetime
derivatives are irrelevant for the component-extraction identities checked
here, so D and bar D reduce to their Grassmann-derivative parts.
"""

from __future__ import annotations

import sys
from itertools import combinations
from typing import TypeAlias


Monomial: TypeAlias = tuple[int, ...]
Polynomial: TypeAlias = dict[Monomial, complex]


def clean(polynomial: Polynomial) -> Polynomial:
    return {
        monomial: coefficient
        for monomial, coefficient in polynomial.items()
        if coefficient != 0
    }


def add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = left.copy()
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
    return clean(result)


def scale(coefficient: complex, polynomial: Polynomial) -> Polynomial:
    return clean(
        {
            monomial: coefficient * value
            for monomial, value in polynomial.items()
        }
    )


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            if set(left_monomial) & set(right_monomial):
                continue
            inversions = sum(
                left_index > right_index
                for left_index in left_monomial
                for right_index in right_monomial
            )
            monomial = tuple(sorted(left_monomial + right_monomial))
            coefficient = (
                left_coefficient
                * right_coefficient
                * (-1) ** inversions
            )
            result[monomial] = result.get(monomial, 0) + coefficient
    return clean(result)


def left_derivative(index: int, polynomial: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for monomial, coefficient in polynomial.items():
        if index not in monomial:
            continue
        position = monomial.index(index)
        differentiated = monomial[:position] + monomial[position + 1 :]
        result[differentiated] = (
            result.get(differentiated, 0)
            + coefficient * (-1) ** position
        )
    return clean(result)


VARIABLES = tuple({(index,): 1} for index in range(4))
ONE: Polynomial = {(): 1}


def d_squared(polynomial: Polynomial) -> Polynomial:
    # D_alpha=-partial/partial theta^alpha and
    # D^alpha D_alpha=2 D_1 D_2.
    return scale(
        2,
        left_derivative(0, left_derivative(1, polynomial)),
    )


def bar_d_squared(polynomial: Polynomial) -> Polynomial:
    # bar D_dotalpha=partial/partial bar theta^dotalpha and
    # bar D_dotalpha bar D^dotalpha=-2 bar D_dot1 bar D_dot2.
    return scale(
        -2,
        left_derivative(2, left_derivative(3, polynomial)),
    )


def conjugate(polynomial: Polynomial) -> Polynomial:
    # Complex conjugation reverses Grassmann order and interchanges
    # theta^alpha with bar theta^dotalpha.
    conjugate_index = {0: 2, 1: 3, 2: 0, 3: 1}
    result: Polynomial = {}
    for monomial, coefficient in polynomial.items():
        conjugated_term: Polynomial = {(): coefficient.conjugate()}
        for index in reversed(monomial):
            conjugated_term = multiply(
                conjugated_term,
                VARIABLES[conjugate_index[index]],
            )
        result = add(result, conjugated_term)
    return clean(result)


def require_equal(
    name: str,
    actual: Polynomial,
    expected: Polynomial,
) -> None:
    if clean(actual) != clean(expected):
        print(f"FAIL: {name}")
        print("actual:", clean(actual))
        print("expected:", clean(expected))
        raise AssertionError(name)
    print(f"OK: {name}")


def main() -> int:
    theta_squared = scale(
        2,
        multiply(VARIABLES[0], VARIABLES[1]),
    )
    bar_theta_squared = scale(
        -2,
        multiply(VARIABLES[2], VARIABLES[3]),
    )
    highest_monomial = scale(
        1 / 2,
        multiply(theta_squared, bar_theta_squared),
    )

    require_equal(
        "D^2(theta^2)=-4",
        d_squared(theta_squared),
        scale(-4, ONE),
    )
    require_equal(
        "bar D^2(bar theta^2)=-4",
        bar_d_squared(bar_theta_squared),
        scale(-4, ONE),
    )
    require_equal(
        "[bar D^2 h]_F=-2[h]_D",
        bar_d_squared(highest_monomial),
        scale(-2, theta_squared),
    )

    for degree in (0, 2, 4):
        for monomial in combinations(range(4), degree):
            test_polynomial = {monomial: 1}
            require_equal(
                "(bar D^2 S)^*=D^2 S^* "
                f"for even monomial {monomial}",
                conjugate(bar_d_squared(test_polynomial)),
                d_squared(conjugate(test_polynomial)),
            )

    print("All ordered superspace convention checks passed.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError:
        sys.exit(1)
