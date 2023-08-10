#!/usr/bin/env bash
set -x
workspace_folder=$1
mkdir -m 755 -p .devcontainer/assets || echo ""
echo "USER_ID=$(id -u)" > .devcontainer/assets/setup.env

git config oh-my-zsh.hide-dirty 1

git config --global --add safe.directory "${workspace_folder}"
