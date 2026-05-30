# Ranpaper

A easy to use wallpaper utility designed to work with multiple daemons in a minimalist style.

## Installation

Ranpaper comes in multiple shapes and sizes.

### Shell Script (Recommend)

Open your terminal and paste this shell script to install ranpaper.

```sh
curl -fsSL https://raw.githubusercontent.com/gr3yt/ranpaper/main/install.sh | bash
```

### Package Managers

Coming Soon

## Uninstall

### Shell Script (Recommend)

Open your terminal and paste this shell script to install ranpaper.

```sh
curl -fsSL https://raw.githubusercontent.com/gr3yt/ranpaper/main/uninstall.sh | bash
```

### Package Managers

Coming Soon

## Documentation

### Usage

In a terminal you can run the help command to get instructions on each command

```sh
ranpaper -h
```

### Config

The config file is written in the TOML format and its located at `~/.config/ranpaper.toml`

#### General 

- `auto-generated` tells the program if the config has been edited yet.
- `kittyimages` if true enables image preview when listing images using kittys image API
- `imagewidth` the width of pixels used in a image preview

#### Paths

- `wallpaper-dir` the directory with all the wallpapers

#### Wallpaper

- `wallpaper-daemon` the daemon selected to be used
- `awww-transition-type` awww daemon transition type
- `awww-transition-step` awww daemon step amount
- `awww-transition-fps` awww daemon fps
- `awww-transition-angle` awww daemon angle

## Showcase

![alt text](https://raw.githubusercontent.com/gr3yt/ranpaper/main/assets/imagelist.jpg "Images in list")
