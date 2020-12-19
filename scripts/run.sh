#!/bin/bash

set -eu

REPO_ROOT_DIR=$(git rev-parse --show-toplevel)

docker build -t taqueria-bonjour:latest "$REPO_ROOT_DIR"

docker run \
    --rm \
    -p 8080:8080 \
    -e TWILIO_ACCOUNT_SID=$(sops -d --extract '["twilio_account_sid"]' secrets/twilio.yaml) \
    -e TWILIO_AUTH_TOKEN=$(sops -d --extract '["twilio_auth_token"]' secrets/twilio.yaml) \
    -e TWILIO_ORIGIN_NUMBER=$(sops -d --extract '["origin_number"]' secrets/twilio.yaml) \
    -it taqueria-bonjour:latest
