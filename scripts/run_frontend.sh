#!/bin/bash

set -eu

REPO_ROOT_DIR=$(git rev-parse --show-toplevel)

docker build -t taqueria-bonjour-frontend:latest "$REPO_ROOT_DIR/frontend"

docker run \
    --rm \
    -v ${REPO_ROOT_DIR}/frontend:/src \
    -v /src/node_modules \
    -p 3000:3000 \
    -e CHOKIDAR_USEPOLLING=true \
    -it taqueria-bonjour-frontend:latest
