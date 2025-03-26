#!/bin/bash

set -euo pipefail

LATEST_TAG=$(git describe --tags --abbrev=0)

VERSION=${LATEST_TAG#v}

IFS='.' read -r -a VERSION_PARTS <<< "$VERSION"

MAJOR=${VERSION_PARTS[0]}
MINOR=${VERSION_PARTS[1]}
PATCH=${VERSION_PARTS[2]}

NEW_PATCH=$((PATCH + 1))

NEW_VERSION="$MAJOR.$MINOR.$NEW_PATCH"

echo "v$NEW_VERSION" > version.txt

echo "Current tag: $LATEST_TAG"
echo "New version: v$NEW_VERSION"
