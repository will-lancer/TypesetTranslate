#!/usr/bin/env python3
"""Small fail-closed tests for the standalone release auditor."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "scripts"))
import audit_release_pipeline as audit  # noqa: E402
import check_reproducibility as reproducibility  # noqa: E402
import check_transcription_review as transcription_review  # noqa: E402
import generate_review_provenance as provenance_generator  # noqa: E402


class ReleasePipelineTests(unittest.TestCase):
    def test_input_tree_hash_excludes_generated_and_release_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "latex").mkdir()
            (root / "work" / "rendered-output").mkdir(parents=True)
            (root / "source.tex").write_text("alpha\n", encoding="utf-8")
            (root / "latex" / "master.pdf").write_bytes(b"generated")
            (root / "latex" / "master.synctex.gz").write_bytes(b"generated")
            (root / "work" / "rendered-output" / "page-1.png").write_bytes(b"generated")
            (root / "RELEASE_VERIFICATION.md").write_text("later\n", encoding="utf-8")
            (root / "review-coverage.json").write_text(
                json.dumps({"records": [{"id": "pass-4-release", "status": "pending"}]}),
                encoding="utf-8",
            )
            first, entries = audit.deterministic_input_tree_hash(root)
            (root / "latex" / "master.pdf").write_bytes(b"changed generated")
            (root / "latex" / "master.synctex.gz").write_bytes(b"changed generated")
            (root / "work" / "rendered-output" / "page-1.png").write_bytes(b"changed generated")
            (root / "RELEASE_VERIFICATION.md").write_text("changed record\n", encoding="utf-8")
            (root / "review-coverage.json").write_text(
                json.dumps({"records": [{"id": "pass-4-release", "status": "pass"}]}),
                encoding="utf-8",
            )
            second, _ = audit.deterministic_input_tree_hash(root)
            self.assertEqual(first, second)
            self.assertEqual(
                ["review-coverage.json", "source.tex"],
                [line.split("  ", 1)[1] for line in entries],
            )
            (root / "source.tex").write_text("beta\n", encoding="utf-8")
            third, _ = audit.deterministic_input_tree_hash(root)
            self.assertNotEqual(first, third)

    def test_pending_coverage_records_block(self) -> None:
        manifest = json.loads((PROJECT / "review-coverage.json").read_text(encoding="utf-8"))
        manifest["source_ranges"][0]["status"] = "pending"
        manifest["figures"][-1]["status"] = "pending"
        manifest["global_audits"][-1]["status"] = "pending"
        manifest["required_pass_records"][-1]["status"] = "pending"
        with tempfile.TemporaryDirectory() as directory:
            manifest_path = Path(directory) / "review-coverage.json"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            failures = audit.coverage_failures(root=PROJECT, manifest_path=manifest_path)
        self.assertTrue(any("source_ranges[1] status is 'pending'" in item for item in failures))
        self.assertTrue(any("figures[13] status is 'pending'" in item for item in failures))
        self.assertTrue(any("global_audits[4] status is 'pending'" in item for item in failures))
        self.assertTrue(any("required_pass_records[4] status is 'pending'" in item for item in failures))
        self.assertEqual(
            [
                "work/reviews/PASS_1_RECONSTRUCT.md",
                "work/reviews/PASS_2_TECHNICAL.md",
                "work/reviews/PASS_3_ADVERSARIAL.md",
                "work/reviews/PASS_4_RELEASE.md",
            ],
            [record["review_files"][0] for record in manifest["required_pass_records"]],
        )
        required_fields = [
            "PASS:",
            "INPUT SNAPSHOT:",
            "FULL SCOPE READ:",
            "FINDINGS:",
            "EDITS MADE:",
            "CHECKS RUN:",
            "UNRESOLVED:",
            "STATUS: PASS",
            "Unresolved blockers: none",
        ]
        self.assertEqual(
            [required_fields] * 4,
            [record["required_fields"] for record in manifest["required_pass_records"]],
        )
        inventory = next(record for record in manifest["global_audits"] if record["id"] == "object-inventory")
        self.assertEqual(5, len(inventory["review_files"]))

    def test_review_provenance_requires_coverage_declared_review_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            coverage = root / "review-coverage.json"
            coverage.write_text(
                json.dumps(
                    {
                        "source_ranges": [
                            {"review_files": ["work/reviews/required.md"]}
                        ]
                    }
                ),
                encoding="utf-8",
            )
            failures = audit.required_review_record_failures(root, coverage)
            self.assertTrue(any("required.md" in item for item in failures))
            required = root / "work" / "reviews" / "required.md"
            required.parent.mkdir(parents=True)
            required.write_text("Unresolved blockers: none\n", encoding="utf-8")
            self.assertEqual([], audit.required_review_record_failures(root, coverage))

    def test_generated_pass4_record_uses_writing_audit_fields(self) -> None:
        text = audit.pass4_release_text(
            {
                "input_tree_sha256": "a" * 64,
                "verified_pdf_sha256": "b" * 64,
                "exported_pdf_sha256": "b" * 64,
                "page_count": 186,
                "inspected_count": 186,
                "reviewers": ["reviewer"],
            }
        )
        for field in json.loads(
            (PROJECT / "review-coverage.json").read_text(encoding="utf-8")
        )["required_pass_records"][3]["required_fields"]:
            self.assertIn(field, text)
        self.assertEqual(1, text.count("Unresolved blockers: none"))

    def test_generated_release_record_numeric_fields_match_the_parser(self) -> None:
        text = audit.release_record_text(
            {
                "source_sha256": "a" * 64,
                "input_tree_sha256": "b" * 64,
                "verified_pdf_sha256": "c" * 64,
                "exported_pdf_sha256": "c" * 64,
                "page_count": 180,
                "render_dpi": 180,
                "inspected_count": 180,
                "reviewers": ["reviewer"],
                "warnings": [],
                "image_count": 0,
                "font_count": 50,
                "text_chars": 421115,
            }
        )
        patterns = (
            r"^- Native PDF page count:\s*`(\d+)`\s*$",
            r"^- Render DPI:\s*`(\d+)`\s*$",
            r"^- Pages rendered:\s*`(\d+)`\s*$",
            r"^- Pages visually inspected:\s*`(\d+)`\s*$",
        )
        self.assertEqual(["180"] * 4, [re.search(pattern, text, re.MULTILINE).group(1) for pattern in patterns])

    def test_warning_allowlist_is_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            log = root / "master.log"
            allowlist = root / "allowlist.json"
            log.write_text("Package hyperref Warning: test diagnostic.\n", encoding="utf-8")
            allowlist.write_text(json.dumps({"schema_version": 1, "allowed": []}), encoding="utf-8")
            failures, accepted = audit.warning_failures(log, allowlist)
            self.assertEqual([], accepted)
            self.assertTrue(any("Unallowlisted" in item for item in failures))
            allowlist.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "allowed": [{"pattern": "hyperref Warning", "reason": "reviewed test"}],
                    }
                ),
                encoding="utf-8",
            )
            failures, accepted = audit.warning_failures(log, allowlist)
            self.assertEqual([], failures)
            self.assertEqual(1, len(accepted))

    def test_fls_parser_keeps_local_inputs_and_drops_system_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fls = root / "master.fls"
            fls.write_text(
                "\n".join(
                    [
                        f"PWD {root}",
                        "INPUT /usr/local/texlive/texmf.cnf",
                        "INPUT master.tex",
                        "INPUT ./figures/fig1_1.tex",
                        "INPUT figures/fig1_1.tex",
                        f"INPUT {root / 'pct.sty'}",
                    ]
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                {"master.tex", "figures/fig1_1.tex", "pct.sty"},
                audit.parse_fls_inputs(fls),
            )

    def test_template_release_record_is_not_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            template = Path(directory) / "RELEASE_VERIFICATION.md"
            template.write_text(
                "# Release verification record\n\n"
                "- Source SHA-256: `[populate after source audit]`\n",
                encoding="utf-8",
            )
            failures = audit.release_record_failures(record_path=template)
        self.assertTrue(any("placeholder" in item.lower() for item in failures))

    def test_preflight_skips_a_stale_existing_export(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            verified = root / "master.pdf"
            exported = root / "release.pdf"
            verified.write_bytes(b"current")
            exported.write_bytes(b"stale")
            failures, evidence = audit.export_failures(
                verified_pdf=verified,
                export_pdf=exported,
                require_export=False,
            )
            expected_hash = audit.sha256(verified)
        self.assertEqual([], failures)
        self.assertEqual(expected_hash, evidence["verified_pdf_sha256"])
        self.assertNotIn("exported_pdf_sha256", evidence)

    def test_reproducibility_environment_is_fixed(self) -> None:
        self.assertEqual(
            reproducibility.EXPECTED_ENV,
            reproducibility.load_fixed_environment(),
        )

    def test_missing_reproducibility_evidence_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            original = audit.REPRODUCIBILITY_EVIDENCE
            audit.REPRODUCIBILITY_EVIDENCE = Path(directory) / "missing.json"
            try:
                failures, _ = audit.reproducibility_failures()
            finally:
                audit.REPRODUCIBILITY_EVIDENCE = original
        self.assertTrue(any("Missing JSON data file" in item for item in failures))

    def test_only_finalizer_owned_records_can_be_pending_during_preflight(self) -> None:
        failures = audit.coverage_failures(
            allow_pending_ids={"pass-4-release", "export-byte-identity"}
        )
        self.assertFalse(any("required_pass_records[4] status" in item for item in failures))
        self.assertFalse(any("release_evidence_requirements[4] status" in item for item in failures))
        self.assertFalse(any("PASS_4_RELEASE.md" in item for item in failures))

    def test_reproducibility_bytes_and_pages_match_current_master(self) -> None:
        evidence = json.loads(audit.REPRODUCIBILITY_EVIDENCE.read_text(encoding="utf-8"))
        evidence["builds"][0]["bytes"] = 1
        evidence["builds"][1]["bytes"] = 2
        evidence["builds"][0]["pages"] = 1
        evidence["builds"][1]["pages"] = 2
        with tempfile.TemporaryDirectory() as directory:
            evidence_path = Path(directory) / "reproducibility.json"
            evidence_path.write_text(json.dumps(evidence), encoding="utf-8")
            original = audit.REPRODUCIBILITY_EVIDENCE
            audit.REPRODUCIBILITY_EVIDENCE = evidence_path
            try:
                failures, _ = audit.reproducibility_failures()
            finally:
                audit.REPRODUCIBILITY_EVIDENCE = original
        self.assertTrue(any("build byte counts differ" in item for item in failures))
        self.assertTrue(any("byte count does not match current master.pdf" in item for item in failures))
        self.assertTrue(any("build page counts differ" in item for item in failures))
        self.assertTrue(any("page count does not match current master.pdf" in item for item in failures))

    def test_pdfimages_empty_or_malformed_output_blocks(self) -> None:
        outputs = ("", "page num type\n")
        for output in outputs:
            result = subprocess.CompletedProcess(
                ["pdfimages", "-list"], 0, output, ""
            )
            with self.subTest(output=repr(output)), patch.object(audit, "run_checked", return_value=result):
                failures, _ = audit.image_failures()
            self.assertTrue(any("table header" in item for item in failures))
            self.assertTrue(any("table separator" in item for item in failures))

    def test_review_provenance_rejects_stale_review_record_hash(self) -> None:
        provenance = json.loads((PROJECT / "review-provenance.json").read_text(encoding="utf-8"))
        provenance["review_records_sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review-provenance.json"
            path.write_text(json.dumps(provenance), encoding="utf-8")
            with patch.object(audit, "source_page_rerender_failures", return_value=[]):
                failures = audit.review_provenance_failures(
                    root=PROJECT, provenance_path=path, require_pdf=False
                )
        self.assertTrue(any("review-record SHA-256" in item for item in failures))

    def test_review_provenance_rejects_empty_review_set(self) -> None:
        with (
            patch.object(audit, "review_record_paths", return_value=[]),
            patch.object(audit, "source_page_rerender_failures", return_value=[]),
        ):
            failures = audit.review_provenance_failures(require_pdf=False)
        self.assertTrue(any("has no review records" in item for item in failures))

    def test_review_provenance_rejects_stale_native_input_hash(self) -> None:
        provenance = json.loads((PROJECT / "review-provenance.json").read_text(encoding="utf-8"))
        provenance["native_input_sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review-provenance.json"
            path.write_text(json.dumps(provenance), encoding="utf-8")
            with patch.object(audit, "source_page_rerender_failures", return_value=[]):
                failures = audit.review_provenance_failures(
                    root=PROJECT, provenance_path=path, require_pdf=False
                )
        self.assertTrue(any("native-input SHA-256" in item for item in failures))

    def test_source_page_provenance_rejects_stale_image_digest(self) -> None:
        provenance = json.loads((PROJECT / "review-provenance.json").read_text(encoding="utf-8"))
        provenance["source_pages"]["sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review-provenance.json"
            path.write_text(json.dumps(provenance), encoding="utf-8")
            with patch.object(audit, "source_page_rerender_failures", return_value=[]):
                failures = audit.review_provenance_failures(
                    root=PROJECT, provenance_path=path, require_pdf=False
                )
        self.assertTrue(any("source-page SHA-256" in item for item in failures))

    def test_source_provenance_rejects_altered_image_even_when_rehashed(self) -> None:
        provenance = json.loads((PROJECT / "review-provenance.json").read_text(encoding="utf-8"))
        altered_digest = "0" * 64
        provenance["source_pages"]["sha256"] = altered_digest
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review-provenance.json"
            path.write_text(json.dumps(provenance), encoding="utf-8")
            with (
                patch.object(audit, "source_page_hash", return_value=(altered_digest, [], 221)),
                patch.object(
                    audit,
                    "source_page_rerender_failures",
                    return_value=["Source-page rerender differs from stored review image: pdf-001.jpg"],
                ),
            ):
                failures = audit.review_provenance_failures(
                    root=PROJECT, provenance_path=path, require_pdf=False
                )
        self.assertTrue(any("rerender differs" in item for item in failures))

    def test_source_page_rerender_rejects_altered_stored_image(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            image_dir = Path(directory) / "source-pages"
            image_dir.mkdir()
            source_image = PROJECT / "work" / "source-pages" / "pdf-001.jpg"
            target = image_dir / "pdf-001.jpg"
            shutil.copyfile(source_image, target)
            altered = bytearray(target.read_bytes())
            altered[100] ^= 1
            target.write_bytes(altered)
            original_pages = audit.EXPECTED_SOURCE_PAGES
            audit.EXPECTED_SOURCE_PAGES = 1
            try:
                failures = audit.source_page_rerender_failures(
                    root=PROJECT, source_pages_dir=image_dir
                )
            finally:
                audit.EXPECTED_SOURCE_PAGES = original_pages
        self.assertTrue(any("rerender differs" in item for item in failures))

    def test_provenance_generator_rejects_stale_page_review_pdf_hashes(self) -> None:
        inspections, failures = audit.read_jsonl(
            PROJECT / "work" / "reviews" / "page-inspection.jsonl"
        )
        self.assertEqual([], failures)
        stale_inspections = [dict(record) for record in inspections]
        stale_inspections[0]["pdf_sha256"] = "0" * 64
        with (
            patch.object(audit, "source_page_rerender_failures", return_value=[]),
            patch.object(audit, "read_jsonl", return_value=(stale_inspections, [])),
        ):
            _, failures = provenance_generator.current_provenance(PROJECT)
        self.assertTrue(any("page-inspection PDF checksum" in item for item in failures))

    def test_source_page_hash_rejects_empty_or_malformed_jpeg(self) -> None:
        for payload, needle in ((b"", "empty source review image"), (b"not-jpeg", "malformed JPEG")):
            with self.subTest(payload=payload), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                image_dir = root / "work" / "source-pages"
                image_dir.mkdir(parents=True)
                (image_dir / "pdf-001.jpg").write_bytes(payload)
                original_pages = audit.EXPECTED_SOURCE_PAGES
                audit.EXPECTED_SOURCE_PAGES = 1
                try:
                    _, failures, _ = audit.source_page_hash(root)
                finally:
                    audit.EXPECTED_SOURCE_PAGES = original_pages
            self.assertTrue(any(needle in item for item in failures))

    def test_visual_reviewer_map_rejects_out_of_range_assignment(self) -> None:
        mapping = json.loads((PROJECT / "visual-reviewer-map.json").read_text(encoding="utf-8"))
        mapping["reviewers"][0]["pdf_pages"] = "002-019"
        inspections = [
            json.loads(line)
            for line in audit.INSPECTION_MANIFEST.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        with tempfile.TemporaryDirectory() as directory:
            mapping_path = Path(directory) / "visual-reviewer-map.json"
            mapping_path.write_text(json.dumps(mapping), encoding="utf-8")
            failures = audit.visual_reviewer_failures(
                set(range(1, 181)), inspections, root=PROJECT, mapping_path=mapping_path
            )
        self.assertTrue(any("missing=[1]" in item or "overlaps page 19" in item for item in failures))
        self.assertTrue(any("outside reviewer range" in item for item in failures))

    def test_visual_reviewer_map_rejects_unknown_reviewer(self) -> None:
        inspections = [
            json.loads(line)
            for line in audit.INSPECTION_MANIFEST.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        inspections[0]["reviewer"] = "unapproved-reviewer"
        failures = audit.visual_reviewer_failures(set(range(1, 181)), inspections)
        self.assertTrue(any("unauthorized reviewer" in item for item in failures))

    def test_visual_reviewer_map_accepts_corrected_agent_ids(self) -> None:
        mapping = json.loads((PROJECT / "visual-reviewer-map.json").read_text(encoding="utf-8"))
        ids_by_range = {entry["pdf_pages"]: entry["id"] for entry in mapping["reviewers"]}
        self.assertEqual("visual_pages_001_019", ids_by_range["001-018"])
        self.assertEqual("visual_pages_077_095", ids_by_range["073-090"])
        self.assertEqual("visual_pages_096_114", ids_by_range["091-108"])
        inspections = [
            json.loads(line)
            for line in audit.INSPECTION_MANIFEST.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        self.assertEqual([], audit.visual_reviewer_failures(set(range(1, 181)), inspections))

    def test_transcription_review_rejects_stale_provenance(self) -> None:
        provenance = json.loads((PROJECT / "review-provenance.json").read_text(encoding="utf-8"))
        provenance["review_records_sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review-provenance.json"
            path.write_text(json.dumps(provenance), encoding="utf-8")
            with (
                patch.object(audit, "source_page_rerender_failures", return_value=[]),
                patch.object(audit, "review_pdf_hash_failures", return_value=[]),
            ):
                result = transcription_review.main(
                    ["--strict", "--root", str(PROJECT), "--provenance", str(path)]
                )
        self.assertEqual(1, result)


if __name__ == "__main__":
    unittest.main()
