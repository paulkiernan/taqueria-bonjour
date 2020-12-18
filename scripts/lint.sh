#!/bin/bash

set -eu

REPO_ROOT_DIR=$(git rev-parse --show-toplevel)

docker run \
    --rm \
    -e OUTPUT_DETAILS=detailed \
    -e RUN_LOCAL=true \
    -e VALIDATE_ALL_CODEBASE=true \
    -e VALIDATE_PYTHON=true \
    -e VALIDATE_DOCKERFILE=true \
    -e VALIDATE_JSON=true \
    -e VALIDATE_YAML=true \
    -v "$REPO_ROOT_DIR":/tmp/lint \
    github/super-linter
