#!/bin/bash
cd "$(dirname "$0")"
if ! command -v node >/dev/null 2>&1; then
  if command -v brew >/dev/null 2>&1; then
    echo "Node.js is not installed. Installing it with Homebrew..."
    brew install node
  else
    echo "Node.js is not installed. Install the LTS version from https://nodejs.org and run this again."
    read -r -p "Press Enter to close..."
    exit 1
  fi
fi
node setup/install.mjs
read -r -p "Press Enter to close..."
