#!/bin/bash

set -eu

REPO_ROOT_DIR=$(git rev-parse --show-toplevel)

docker \
    build \
    -t taqueria-bonjour-backend:latest \
    "$REPO_ROOT_DIR/backend" \
    --file backend/Dockerfile

docker run \
    --rm \
    -p 8080:5000 \
    -e FLASK_ENV=development \
    -e FLASK_APP=taqueria_bonjour:main \
    -e TWILIO_ACCOUNT_SID=$(sops -d --extract '["account_sid"]' secrets/twilio.yaml) \
    -e TWILIO_AUTH_TOKEN=$(sops -d --extract '["auth_token"]' secrets/twilio.yaml) \
    -e TWILIO_ORIGIN_NUMBER=$(sops -d --extract '["origin_number"]' secrets/twilio.yaml) \
    -v ${REPO_ROOT_DIR}/backend:/src/ \
    -it taqueria-bonjour-backend:latest \
        flask run --host=0.0.0.0
