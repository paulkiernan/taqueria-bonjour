#!/bin/bash

set -eu

REPO_ROOT_DIR=$(git rev-parse --show-toplevel)

docker \
    build \
    -t taqueria-bonjour-frontend:latest \
    "$REPO_ROOT_DIR/frontend" \
    --file frontend/Dockerfile.prod

docker run \
    --rm \
    -v ${REPO_ROOT_DIR}/frontend:/src \
    -v /src/node_modules \
    -p 3000:80 \
    -it taqueria-bonjour-frontend:latest
