#!/bin/bash

VERSION=$(cat version.txt)
git tag "v$VERSION"
