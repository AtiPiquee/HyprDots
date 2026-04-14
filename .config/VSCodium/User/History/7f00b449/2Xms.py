import os
import subprocess

# Don't forget to make this project match to POP3

from settings import read_settings, write_settings
import files
import cli 

def validate_settings():
    config = read_settings() or {}
    upadated = False

    if not config.get("path"):
        config["path"] = cli.path()
        upadated = True

    if not config.get("command"):
        config["command"] = cli.command()
        upadated = True

    if upadated:
        write_settings(config)

    return config["path"], config["command"]

def read_wallpapers(path):
    image_ext = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif")
    wallpapers = []

    try:
        for file in os.listdir(path):
            if file.lower().endswith(image_ext):
                full_path = os.path.join(path, file)
                if os.path.isfile(full_path):
                    wallpapers.append((file, full_path))
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")

    return wallpapers

def write_sh(command, home):
    with open(f"{home}/wallpaper.sh", "w") as f:
        f.write(command)

def main():
    home = os.environ['HOME']
    path, command = validate_settings()
    wallpapers = read_wallpapers(path)
    
    selected_wall = cli.wallpaper(wallpapers)

    set_wall = f"#!/bin/sh\n{command} {selected_wall}"
    print(set_wall)
    write_sh(set_wall, home)

    subprocess.run([f"{home}/wallpaper.sh"])

    print("New wallpaper has been set !")

if __name__ == "__main__":
    main()
