#!/bin/bash
set -eux

git config diff.sopsdiffer.textconv "sops -d"
