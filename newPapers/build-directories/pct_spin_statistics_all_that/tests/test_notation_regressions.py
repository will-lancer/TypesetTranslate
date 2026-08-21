from __future__ import annotations

import json
import unittest
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]


def load_notation_map() -> list[dict]:
    return [
        json.loads(line)
        for line in (PROJECT / "notation-map.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


class NotationRegressionTests(unittest.TestCase):
    def test_unitary_symmetry_equation_uses_the_transformed_ket_on_both_rhs_slots(self) -> None:
        text = (PROJECT / "latex/chapters/chapter01/sec1_3.tex").read_text(encoding="utf-8")
        start = text.index(r"\label{eq:ch1-unitary-symmetry-inner-product}")
        block = text[max(0, start - 400) : start + 200]
        self.assertIn(r"\bra{\Phi}\widehat A\ket{\Phi}", block)
        self.assertIn(r"\bra{\widehat\Phi}A\ket{\widehat\Phi}", block)
        self.assertNotIn(r"\ket{\widehat\Phi}A\ket{\Phi}", block)

    def test_massive_thirring_bilinears_use_the_house_dirac_bar(self) -> None:
        text = (PROJECT / "latex/appendix/local-algebras.tex").read_text(encoding="utf-8")
        self.assertIn(r"(-\ii\gamma^\mu\partial_\mu+m)\psi", text)
        self.assertIn(r":\!\bar\psi(x)\gamma^\mu\psi(x)\!:", text)
        self.assertIn(r"Q=\int\dd x\,:\!\bar\psi(x)\gamma^0\psi(x)\!:", text)
        self.assertNotIn(r"\psi^\dagger\gamma", text)

    def test_spinor_star_ledger_points_to_source_pdf_31(self) -> None:
        records = load_notation_map()
        record = next(
            item
            for item in records
            if item.get("rule") == "adjoint.conjugate.spinor-context"
        )
        self.assertEqual({"pdf": 31, "print": 19}, record["source_page"])
        self.assertEqual(31, record["pdf_page"])

    def test_high_risk_formula_records_have_exact_native_locators(self) -> None:
        records = load_notation_map()
        locators = {
            item.get("scope", {}).get("locator")
            for item in records
            if isinstance(item.get("scope"), dict)
        }
        expected = {
            "PCT-SOURCE pdf=028 print=16; eq:1-28; current lines 570-575",
            "PCT-SOURCE pdf=103 print=91; eq:2-114; current lines 473-477",
            "PCT-SOURCE pdf=103 print=91; display id=2-6-formal-fourier; current lines 497-506",
            "PCT-SOURCE pdf=103 print=91; display id=2-6-translation-eigenvalue; current lines 509-513",
            "PCT-SOURCE pdf=104 print=92; display id=2-6-snag-integral; current lines 523-526",
            "PCT-SOURCE pdf=104 print=92; display id=2-6-fourier-inverse; current lines 558-562",
            "PCT-SOURCE pdf=109 print=97; assumptions prose; current lines 53-58",
            "PCT-SOURCE pdf=121 print=109; display current lines 338-342",
            "PCT-SOURCE pdf=121 print=109; display current lines 347-352",
            "PCT-SOURCE pdf=121 print=109; display current lines 357-364",
            "PCT-SOURCE pdf=128 print=116; Delta-plus display; current lines 930-934",
            "PCT-SOURCE pdf=205 print=193; display id=app-sine-gordon; current lines 220-223",
            "PCT-SOURCE pdf=206 print=194; display id=app-massless-field-equation; current lines 235-238",
            "PCT-SOURCE pdf=206 print=194; displays id=app-massive-thirring and app-boson-fermion-current; current lines 308-324",
            "PCT-SOURCE pdf=207 print=195; display id=app-massive-charge; current lines 329-336",
        }
        self.assertTrue(expected.issubset(locators))


if __name__ == "__main__":
    unittest.main()
