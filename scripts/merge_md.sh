#!/bin/bash

# shellcheck disable=SC2206
MERGE_CONFIG=(
  "en/core.md en/format.md en/system_instructions_consolidated.md"
  "ja/core.md ja/format.md ja/system_instructions_consolidated.md"
)

set -e
set -o pipefail

for CONFIG in "${MERGE_CONFIG[@]}"; do
  # shellcheck disable=SC2206
  CONFIG_ARRAY=($CONFIG)
  OUTPUT_FILE="${CONFIG_ARRAY[-1]}"
  FILES=("${CONFIG_ARRAY[@]:0:$((${#CONFIG_ARRAY[@]} - 1))}")

  FILE_PATHS=()
  for FILE in "${FILES[@]}"; do
    FULL_PATH="${GITHUB_WORKSPACE}/${FILE}"

    if [[ ! -f "$FULL_PATH" ]]; then
      echo "Error: File not found - $FULL_PATH"
      exit 1
    fi

    FILE_PATHS+=("$FULL_PATH")
  done

  OUTPUT_PATH="${GITHUB_WORKSPACE}/${OUTPUT_FILE}"

  > "$OUTPUT_PATH"
  for ((i=0; i<${#FILE_PATHS[@]}; i++)); do
    if ! cat "${FILE_PATHS[i]}" >> "$OUTPUT_PATH"; then
      echo "Error: Failed to merge files into ${OUTPUT_FILE}"
      exit 1
    fi

    if [[ $i -lt $((${#FILE_PATHS[@]} - 1)) ]]; then
      echo "" >> "$OUTPUT_PATH"
      echo "" >> "$OUTPUT_PATH"
    fi
  done

  echo "Successfully merged files into ${OUTPUT_FILE}"
done
