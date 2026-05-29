#!/usr/bin/env bash

set -e

REPO="gr3yt/ranpaper"
BRANCH="main"
RAW="https://raw.githubusercontent.com/$REPO/$BRANCH"
INSTALL_PATH="/usr/local/bin/ranpaper"

echo "== ranpaper installer =="

# Detect package manager and install deps
if command -v pacman &>/dev/null; then
  echo "-> Arch detected"
  sudo pacman -S --needed python python-pillow
  pip install tomli-w --break-system-packages

elif command -v apt &>/dev/null; then
  echo "-> Debian/Ubuntu detected"
  sudo apt install -y python3 python3-pip python3-pil
  pip3 install tomli-w --break-system-packages

elif command -v dnf &>/dev/null; then
  echo "-> Fedora detected"
  sudo dnf install -y python3 python3-pip python3-pillow
  pip3 install tomli-w --break-system-packages

elif command -v zypper &>/dev/null; then
  echo "-> openSUSE detected"
  sudo zypper install -y python3 python3-pip python3-Pillow
  pip3 install tomli-w --break-system-packages

else
  echo "-> Unknown distro, attempting pip only"
  pip3 install Pillow tomli-w --break-system-packages
fi

# Download and install
echo "-> Downloading ranpaper..."
curl -fsSL "$RAW/ranpaper.py" -o /tmp/ranpaper.py

echo "-> Installing to $INSTALL_PATH"
sudo install -Dm755 /tmp/ranpaper.py "$INSTALL_PATH"
rm /tmp/ranpaper.py

echo ""
echo "Done! Run 'ranpaper' to get started."
