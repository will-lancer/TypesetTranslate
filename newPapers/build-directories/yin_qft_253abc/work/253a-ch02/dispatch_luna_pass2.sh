#!/usr/bin/env bash
set -u

project_root="/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/yin_qft_253abc"
codex_bin="/Applications/ChatGPT.app/Contents/Resources/codex"
manifest="$project_root/work/253a-ch02/raw-caption-lane-manifest.jsonl"
output_root="$project_root/work/253a-ch02/cleaned-segments"
log_root="$project_root/work/253a-ch02/agent-logs/pass2"
summary_file="$log_root/status.tsv"

mkdir -p "$output_root" "$log_root"
: > "$summary_file"

task_pids=()
task_labels=()

while IFS=$'\t' read -r lane_id video_id lane_start lane_end input_rel output_rel; do
  prompt="Pass 2 literal transcript-cleanup lane for Xi Yin QFT Chapter 2. Read SOURCE_MANIFEST.yaml, AGENT_POLICY.md, WRITING_STYLE.md, WORKFLOW.md, CHAPTER_PLAN.md, and MASTER_PROMPT.md completely. Read ${input_rel}, work/253a-ch02/source-lanes/video-${video_id}.md, work/253a-ch02/source-lanes/playlist-chronology.md, work/253a-ch02/source-lanes/boundary-assignment.md, and every note-page source lane that the video report maps to this interval. Account for every raw_caption_event in ${input_rel}, in order, with no lexical omissions hidden between records. Group adjacent raw events into coherent spoken units, normally 10 to 45 seconds. Each output line must be one JSON object with record_type transcript_segment; lane_id ${lane_id}; video_id ${video_id}; start and end; source_event_indices as a complete ordered list; raw_text formed from those raw events in order with whitespace normalized only; cleaned_text containing a literal cleanup that removes isolated fillers and immediate false starts, repairs punctuation and high-confidence caption errors, and preserves Xi Yin's wording, questions, jokes, qualifications, and connective tissue; disposition; operations as explicit objects; note_pages; pdf_pages; confidence; uncertainty; and formula_authority. Use null cleaned_text only for logistics, nonspeech, unusable uncertainty, or content outside Chapter 2, and record the complete omitted text and reason in operations. Do not paraphrase, summarize, add explanations, or resolve formulas against outside sources. Finish with a lane_audit metadata object that states input event count, consumed event count, first and last source_event_index, and whether coverage is exact. Write only ${output_rel} using apply_patch. Do not edit canonical LaTeX, other evidence files, scripts, policies, or Chapter 1. Do not spawn agents."

  "$codex_bin" exec \
    --ephemeral \
    -m gpt-5.6-luna \
    -c 'model_reasoning_effort="max"' \
    -c 'service_tier="priority"' \
    -s workspace-write \
    -C "$project_root" \
    -- \
    "$prompt" \
    > "$log_root/$lane_id.log" 2>&1 &

  task_pids+=("$!")
  task_labels+=("$lane_id")
done < <(
  jq -r '[.lane_id,.video_id,.start,.end,.raw_lane_path,.expected_output] | @tsv' "$manifest"
)

for task_index in "${!task_pids[@]}"; do
  task_pid="${task_pids[$task_index]}"
  task_label="${task_labels[$task_index]}"
  if wait "$task_pid"; then
    printf '%s\tcomplete\n' "$task_label" >> "$summary_file"
  else
    task_status="$?"
    printf '%s\tfailed:%s\n' "$task_label" "$task_status" >> "$summary_file"
  fi
done
