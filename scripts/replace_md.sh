#!/bin/bash

NEW_VERSION=$(cat version.txt)

FILES=(
  "en/system_instructions.md"
  "ja/system_instructions.md"
)

for FILE in "${FILES[@]}"; do
  FULL_PATH="${GITHUB_WORKSPACE}/${FILE}"

  if [ -f "$FULL_PATH" ]; then
    sed -i "s/v[0-9]\+\.[0-9]\+\.[0-9]\+/$NEW_VERSION/g" "$FULL_PATH"
    echo "Updated version in $FILE to $NEW_VERSION"
  else
    echo "Warning: File $FILE not found."
  fi
done
