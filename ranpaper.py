#!/usr/bin/env python3 

import os
import tomllib
import tomli_w
import sys
import random
import base64, sys
import subprocess
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

CONFIG_PATH = os.path.expanduser("~/.config/ranpaper.toml")

DEFAULT_CONFIG = {
  "general": {
    "auto-generated": 1,
    "kittyimages": False,
    "imagewidth": 480
  },
  "paths": {
    "wallpaper-dir": "~/wallpapers"
  },
  "wallpaper": {
    "wallpaper-daemon": "hyprpaper",
    "awww-transition-type": "grow",
    "awww-transition-step": 150,
    "awww-transition-fps": 144,
    "awww-transition-angle": 30
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

def changewallpaper(wallpaperp):

  if CFG["wallpaper"]["wallpaper-daemon"] == "awww":
    
    if "-a-help" in sys.argv:
      print("""
--------------------------------------------------
AWWW flags - recomended to set these in the config
--------------------------------------------------

 format
 <ranpaper-flag> ==> <awww=flag>

 -a-type ==> --transition-type
 -a-step ==> --transition-step
 -a-fps ==> --transition-fps
 -a-angle ==> --transition-angle
      """)
      return
    if "-a-type" in sys.argv:
      idx = sys.argv.index("-a-type")
      a_type = sys.argv[idx + 1]
    else:
      a_type = CFG["wallpaper"]["awww-transition-type"]

    if "-a-step" in sys.argv:
      idx = sys.argv.index("-a-step")
      a_step = sys.argv[idx + 1]
    else:
      a_step = CFG["wallpaper"]["awww-transition-step"]

    if "-a-fps" in sys.argv:
      idx = sys.argv.index("-a-fps")
      a_fps = sys.argv[idx + 1]
    else:
      a_fps = CFG["wallpaper"]["awww-transition-fps"]

    if "-a-angle" in sys.argv:
      idx = sys.argv.index("-a-angle")
      a_angle = sys.argv[idx + 1]
    else:
      a_angle = CFG["wallpaper"]["awww-transition-angle"]

    try:
      subprocess.run(
        ["awww", "img", wallpaperp,
         "--transition-type", a_type,
         "--transition-step", str(a_step),
         "--transition-fps", str(a_fps),
         "--transition-angle", str(a_angle)],
        check=True,
        capture_output=True,
        text=True
      )
      print("Set wallaper with AWWW")
    except subprocess.CalledProcessError as e:
      print("ERROR -", e.stderr)
      print("Failed to set wallpeper with AWWW")
      print("Is awww daemon running?")

  elif CFG["wallpaper"]["wallpaper-daemon"] == "hyprpaper":
    try:
      subprocess.run(
        ["hyprctl", "hyprpaper", "wallpaper", ",", wallpaperp],
        check=True,
        capture_output=True,
        text=True
      )
      print("Set wallpaper with hyprpaper")
    except subprocess.CalledProcessError as e:
      print("ERROR -", e.stderr)
      print("Failed to set wallpeper with hyprpaper")
      print("Is hyprpaper running?")
  else:
    print("Invalid wallpaper daemon set")
    print("Only supported daemons in this version is:")
    print("hyprpaper")
    print("awww")
    print("\nIf you would like to request a new daemon option please request it via github issues.")


def app():
  if CFG["general"]["auto-generated"] == 1:
    print("Your config is auto generated!")
    print("\nPlease go to", CONFIG_PATH, "and configure your setup")
    print("Once setup is finished set 'auto-generated' to 0")
    print("\nURGENT - Default daemon is set to hyprpaper. Please change this in the config in the value 'wallpaper-daemon'")
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
      changewallpaper(wallpaper_path)
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
      changewallpaper(wallpaper_path)
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

 -- ranpaper -a-help
  - shows help with setting awww flags via ranpaper

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
  changewallpaper(wallpaper_path)



app()

