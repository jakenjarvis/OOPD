#!/bin/bash

set -euo pipefail

LATEST_TAG=$(git describe --tags --abbrev=0)

VERSION=${LATEST_TAG#v}

IFS='.' read -r -a VERSION_PARTS <<< "$VERSION"

MAJOR=${VERSION_PARTS[0]}
MINOR=${VERSION_PARTS[1]}
PATCH=${VERSION_PARTS[2]}

LATEST_COMMIT_MESSAGE=$(git log -1 --pretty=%B)

if [[ "$LATEST_COMMIT_MESSAGE" == *'#version:v'* ]]; then
  NEW_VERSION=$(echo "$LATEST_COMMIT_MESSAGE" | sed -E 's/.*#version:(v[0-9]+\.[0-9]+\.[0-9]+).*/\1/')
  VERSION_PARTS=(${NEW_VERSION#v//. })
  MAJOR=${VERSION_PARTS[0]}
  MINOR=${VERSION_PARTS[1]}
  PATCH=${VERSION_PARTS[2]}
else
  PATCH=$((PATCH + 1))
  NEW_VERSION="v$MAJOR.$MINOR.$PATCH"
fi

echo "Current tag: $LATEST_TAG"
echo "New version: $NEW_VERSION"

echo "$NEW_VERSION" > version.txt
