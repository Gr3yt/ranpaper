#!/bin/bash

set -e

# CONFIG
REPO_URL="https://raw.githubusercontent.com/Gr3yt/ranpaper/main"
SCRIPT_NAME="ranpaper"
INSTALL_PATH="/usr/local/bin/$SCRIPT_NAME"

sudo curl -fsSL "$REPO_URL/$SCRIPT_NAME" -o "$INSTALL_PATH"
sudo chmod +x "$INSTALL_PATH"

echo "Ranpaper is successfully installed!
You can now open the help menu by running: $SCRIPT_NAME -h"
