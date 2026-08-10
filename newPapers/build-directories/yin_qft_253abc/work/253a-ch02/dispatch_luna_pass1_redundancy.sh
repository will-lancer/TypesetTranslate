#!/usr/bin/env bash
set -u

project_root="/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/yin_qft_253abc"
codex_bin="/Applications/ChatGPT.app/Contents/Resources/codex"
log_root="$project_root/work/253a-ch02/agent-logs/pass1-redundancy"
status_file="$log_root/status.tsv"

mkdir -p "$log_root"
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

common="Read SOURCE_MANIFEST.yaml, AGENT_POLICY.md, WRITING_STYLE.md, WORKFLOW.md, CHAPTER_PLAN.md, and MASTER_PROMPT.md completely. This is a Luna Max Fast Pass 1 source task. Preserve source order and ambiguity. Do not consult outside physics sources. Do not edit Chapter 1, master.tex, policies, scripts outside work/253a-ch02, or canonical Chapter 2 files. Write only the named output using apply_patch. Do not spawn agents."

launch "notes-exact-b-alt" "$common Independently read work/253a-ch02/source-lanes/notes-041-042.md through notes-061-062.md and their cited physical-page renders. Produce work/253a-ch02/synthesis-lanes/notes-exact-b-alt.tex as a complete exact source-layer TeX transcription for original note pages 30-51, physical pages 41-62. Follow work/pilot/notes-exact.tex conventions. Include every reported heading, prose fragment, formula, correction, arrow, meaningful color, diagram, qualification, punctuation mark, and page transition. Use exactly one \\YinPageBoundary{original}{physical} per page. Tie open readings to work/253a-ch02/ambiguities.md in comments."

launch "pass1-coverage-audit" "$common Audit the completed Pass 1 evidence under work/253a-ch02. Read source-map.md, chapter-metadata.json, playlist.jsonl, alignment.jsonl, all source-lanes, synthesis-lanes/page-dispositions.jsonl, synthesis-lanes/notes-ambiguities.md, transcript.raw.vtt, and the raw caption-lane manifest. Check exact coverage of physical pages 20-62, exclusion of 63-67, use of page 68 as the next boundary, chronological lecture identity, exact start and end timestamps, caption/raw-source hashes when recorded, and absence of missing or duplicate note pages. Write work/253a-ch02/pass1-coverage-audit.md with evidence-backed findings. End with either Unresolved blockers: none or an exact blocker list. Do not assume notes-exact-b exists yet and report that file as pending rather than a blocker."

for index in "${!pids[@]}"; do
  if wait "${pids[$index]}"; then
    printf '%s\tcomplete\n' "${labels[$index]}" >> "$status_file"
  else
    code="$?"
    printf '%s\tfailed:%s\n' "${labels[$index]}" "$code" >> "$status_file"
  fi
done
