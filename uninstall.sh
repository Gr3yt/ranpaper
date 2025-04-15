#!/bin/bash

set -e

SCRIPT_NAME="ranpaper"
INSTALL_PATH="/usr/local/bin/$SCRIPT_NAME"

if [ -f "$INSTALL_PATH" ]; then
  sudo rm "$INSTALL_PATH"
  echo "'$SCRIPT_NAME' has been uninstalled from $INSTALL_PATH."
else
  echo "'$SCRIPT_NAME' is not installed at $INSTALL_PATH."
fi
