#!/usr/bin/env python3 

import os
import tomllib
import tomli_w
import sys
import random
import base64, sys
from PIL import Image

def show_kitty(path, width=40):
  img = Image.open(path).convert("RGBA")
  ratio = width / img.width
  img = img.resize((width, int(img.height * ratio)))

  raw = img.tobytes()
  data = base64.standard_b64encode(raw).decode()
  w, h = img.size

  chunks = [data[i:i+4096] for i in range(0, len(data), 4096)]
  for i, chunk in enumerate(chunks):
    m = 1 if i < len(chunks) - 1 else 0
    header = f"a=T,f=32,s={w},v={h},m={m}" if i == 0 else f"m={m}"
    sys.stdout.write(f"\033_G{header};{chunk}\033\\")

  sys.stdout.write("\n")
  sys.stdout.flush()

CONFIG_PATH = os.path.expanduser("~/.config/hypr/ranpaper.toml")

DEFAULT_CONFIG = {
  "general": {
    "auto-generated": 1,
    "kittyimages": False,
    "imagewidth": 480
  },
  "paths": {
    "wallpaper-dir": "~/wallpapers"
  }
}

def load_config():
  os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)

  if not os.path.exists(CONFIG_PATH):
    print("Config not found auto generating one at:", CONFIG_PATH)
    with open(CONFIG_PATH, "wb") as f:
      tomli_w.dump(DEFAULT_CONFIG, f)
    return DEFAULT_CONFIG

  with open(CONFIG_PATH, "rb") as f:
    return tomllib.load(f)

def save_config(cfg):
  with open(CONFIG_PATH, "wb") as f:
    tomli_w.dump(cfg, f)

CFG = load_config()

def app():
  if CFG["general"]["auto-generated"] == 1:
    print("Your config is auto generated!")
    print("\nPlease go to", CONFIG_PATH, "and configure your setup")
    print("Once setup is finished set 'auto-generated' to 0")
    return

  wallpaper_dir = os.path.expanduser(CFG["paths"]["wallpaper-dir"])
  wallpapers = os.listdir(wallpaper_dir)

  if "-l" in sys.argv:
    if len(wallpapers) == 0:
      print("\n No wallpapers found at -", CFG["paths"]["wallpaper_dir"])
      return

    print("\n List of wallpapers in -", CFG["paths"]["wallpaper-dir"], "\n")
    for w in wallpapers:
      wallpaper_path = f"{wallpaper_dir}/{w}"
      print(f" - {w}")
      if CFG["general"]["kittyimages"] == True:
        show_kitty(wallpaper_path, width=CFG["general"]["imagewidth"])
    return

  if "-s" in sys.argv:
    idx = sys.argv.index("-s")
    sel_wallpaper = sys.argv[idx + 1]
    wallpaper_path = f"{wallpaper_dir}/{sel_wallpaper}"
    if os.path.exists(wallpaper_path):
      os.system(f"hyprctl hyprpaper wallpaper , {wallpaper_path}")
      return

    print("\n Error! \n")
    print(" - Wallpaper not found in the selected directory")
    print(" - Run 'ranpaper -h' for help")
    return
  
  if "-S" in sys.argv:
    idx = sys.argv.index("-S")
    sel_wallpaper = sys.argv[idx + 1]
    wallpaper_path = os.path.expanduser(sel_wallpaper)
    if os.path.exists(wallpaper_path):
      os.system(f"hyprctl hyprpaper wallpaper , {wallpaper_path}")
      return

    print("\n Error! \n")
    print(" - Wallpaper not found in the path entered")
    print(" - Run 'ranpaper -h' for help")
    return

  if "-h" in sys.argv:
    print('''
------------------------------------------------------------
 -- ranpaper - a hyprpaper utility made by greyt
  - config located at - ~/.config/hypr/ranpaper.toml
------------------------------------------------------------
 
 -- ranpaper
  - selects a random wallpaper from the "wallpaper_dir" path from the config file.

 -- ranpaper -l
  - lists wallpapers in the selected wallpaper directory
  
 -- ranpaper -s <image>
  - selects the image entered to use as a wallpaper from the wallpaper directory
  - eg. ranpaper -s city.jpg

 -- ranpaper -s <image>
  - sets the wallpaper to an image chosen in a differnt path.
  - eg. ranpaper -s /home/user/grey/wallpapers/city.jpg

''')
    return

  sel_wallpaper = wallpapers[random.randint(0, len(wallpapers) - 1)]
  wallpaper_path = f"{wallpaper_dir}/{sel_wallpaper}"
  os.system(f"hyprctl hyprpaper wallpaper , {wallpaper_path}")



app()

