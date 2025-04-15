# Ranpaper
The best wallpaper randomizer / selector for hyprpaper.

## Installation 

### Script (recommended)

To install Ranpaper you can run this script 
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Gr3yt/ranpaper/main/install.sh)"
```
### Package manager 

You could also install Ranpaper from these official packages.

- AUR - Soon (hopefully)

## Uninstallation

### script

To uninstall run this script

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Gr3yt/ranpaper/main/uninstall.sh)"
```

### Package manager

If you installed with a package manager, you can get rid of it the usual way.

## Usage

Put usable images that work with hyprpaper into the wallpaper directory (to get the directory run ```ranpaper -p```).
Then run ``` ranpaper ``` to get a randomized wallpaper.

## Flags

To show all flags use ``` ranpaper -h ``` but here are basics

List ``` ranpaper -l ``` lists all the files in the wallpaper folder.
Select ``` ranpaper -s <file> ``` lets you select a specific image from the wallpaper folder as a wallpaper.

## Future Ideas

- [x] Change  wallpaper folder
- [x] Set specific wallpaper
- [ ] auto invalid file detection
