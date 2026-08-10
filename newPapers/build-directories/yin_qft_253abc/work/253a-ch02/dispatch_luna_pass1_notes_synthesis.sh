#!/usr/bin/env bash
set -u

project_root="/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/yin_qft_253abc"
codex_bin="/Applications/ChatGPT.app/Contents/Resources/codex"
log_root="$project_root/work/253a-ch02/agent-logs/pass1-notes-synthesis"
output_root="$project_root/work/253a-ch02/synthesis-lanes"
status_file="$log_root/status.tsv"

mkdir -p "$log_root" "$output_root"
: > "$status_file"

pids=()
labels=()

launch() {
  label="$1"
  prompt="$2"
  "$codex_bin" exec \
    --ephemeral \
    -m gpt-5.6-luna \
    -c 'model_reasoning_effort="max"' \
    -c 'service_tier="priority"' \
    -s workspace-write \
    -C "$project_root" \
    -- \
    "$prompt" \
    > "$log_root/$label.log" 2>&1 &
  pids+=("$!")
  labels+=("$label")
}

common="Read SOURCE_MANIFEST.yaml, AGENT_POLICY.md, WRITING_STYLE.md, WORKFLOW.md, CHAPTER_PLAN.md, and MASTER_PROMPT.md completely. This is Pass 1 source synthesis, so preserve the handwritten source without smoothing it into textbook prose. Use only the specified source-lane reports and their cited rendered pages. Do not consult outside physics sources. Do not edit Chapter 1, master.tex, scripts, policies, or canonical Chapter 2 files. Write only the requested unique output with apply_patch. Do not spawn agents."

launch "notes-exact-a" "$common Read work/253a-ch02/source-lanes/notes-021-022.md through notes-039-040.md, in physical-page order. Produce work/253a-ch02/synthesis-lanes/notes-exact-a.tex as an exact source-layer TeX transcription for original note pages 10-29, combined physical pages 21-40. Follow the macro and page-boundary conventions of work/pilot/notes-exact.tex. Include every heading, prose fragment, formula, bullet, arrow relation, meaningful color, correction, annotation, diagram description or TikZ reconstruction, qualification, question mark, and page transition reported by the lanes. Use one \YinPageBoundary{original}{physical} per page. Preserve ambiguity in TeX comments tied to work/253a-ch02/ambiguities.md."

launch "notes-exact-b" "$common Read work/253a-ch02/source-lanes/notes-041-042.md through notes-061-062.md, in physical-page order. Produce work/253a-ch02/synthesis-lanes/notes-exact-b.tex as an exact source-layer TeX transcription for original note pages 30-51, combined physical pages 41-62. Follow the macro and page-boundary conventions of work/pilot/notes-exact.tex. Include every heading, prose fragment, formula, bullet, arrow relation, meaningful color, correction, annotation, diagram description or TikZ reconstruction, qualification, question mark, and page transition reported by the lanes. Use one \YinPageBoundary{original}{physical} per page. Preserve ambiguity in TeX comments tied to work/253a-ch02/ambiguities.md."

launch "page-dispositions" "$common Read all 21 note-page source-lane reports from notes-021-022.md through notes-061-062.md. Produce work/253a-ch02/synthesis-lanes/page-dispositions.jsonl with exactly one compact JSON object for each original note page 10-51 and physical page 21-62. Give stable IDs YIN253A-C02-PD010 through YIN253A-C02-PD051, note_page, pdf_page, disposition, complete retained_elements, normalized_elements, omitted_elements, reason, confidence, and review_status. At Pass 1, included_unit_ids and normalized_unit_ids must be empty arrays because the chapter units do not exist yet. Every reported source element must appear under retained, normalized, omitted, or unresolved, with no blanket wording."

launch "notes-ambiguities" "$common Read all 21 note-page source-lane reports and work/253a-ch02/source-lanes/boundary-assignment.md. Produce work/253a-ch02/synthesis-lanes/notes-ambiguities.md. Aggregate every uncertain glyph, formula, ink-color meaning, diagram interpretation, cross-page dependency, source correction, possible normalization, physical-page boundary, and assignment-boundary issue. Use a stable ID per issue, cite original and physical pages, quote the competing readings, state the source evidence, and recommend a disposition without silently resolving uncertainty. End with a 42-page coverage table and a zero-omission audit or a precise blocker list."

for index in "${!pids[@]}"; do
  if wait "${pids[$index]}"; then
    printf '%s\tcomplete\n' "${labels[$index]}" >> "$status_file"
  else
    code="$?"
    printf '%s\tfailed:%s\n' "${labels[$index]}" "$code" >> "$status_file"
  fi
done
