#!/usr/bin/env bash

INSTALL_PATH="/usr/local/bin/ranpaper"

echo "== ranpaper uninstall =="

read -p "Are you sure you want to uninstall ranpaper? [y/N] " confirm

if [[ "$confirm" =~ ^[Yy]$ ]]; then
  echo "-> Uninstalling ):"
  rm $INSTALL_PATH
  echo "Uninstalled ranpaper."
else
  echo "Cancelled (:"
  exit 0
fi
