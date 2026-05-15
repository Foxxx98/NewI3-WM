#!/usr/bin/env python3

import os
import random
import subprocess

# ==========================================
# CONFIG
# ==========================================

STATIC_DIR = os.path.expanduser(
    "~/wallpaper_colors_static"
)

ENGINE_DIR = os.path.expanduser(
    "~/wallpaper_colors_engine"
)

STATIC_WALLPAPER_FOLDER = os.path.expanduser(
    "~/Pictures/Wallpapers"
)

WORKSHOP_DIR = os.path.expanduser(
    "~/.steam/steam/steamapps/workshop/content/431960"
)

HDMI_MONITOR = "HDMI-A-1"
DP_MONITOR = "DP-1"

# ==========================================

def get_available_colors():

    static_colors = set(
        f.replace(".txt", "")
        for f in os.listdir(STATIC_DIR)
        if f.endswith(".txt")
    )

    engine_colors = set(
        f.replace(".txt", "")
        for f in os.listdir(ENGINE_DIR)
        if f.endswith(".txt")
    )

    return sorted(static_colors & engine_colors)

def choose_color(colors):

    print("\nColores disponibles:\n")

    for idx, color in enumerate(colors, start=1):
        print(f"{idx}. {color}")

    while True:

        try:
            option = int(input("\nSelecciona un color: "))

            if 1 <= option <= len(colors):
                return colors[option - 1]

        except:
            pass

        print("Opción inválida.")

def random_static_wallpaper(color):

    path = os.path.join(STATIC_DIR, f"{color}.txt")

    with open(path, "r") as f:
        wallpapers = [
            line.strip()
            for line in f.readlines()
            if line.strip()
        ]

    selected = random.choice(wallpapers)

    return os.path.join(
        STATIC_WALLPAPER_FOLDER,
        selected
    )

def random_engine_wallpaper(color):

    path = os.path.join(ENGINE_DIR, f"{color}.txt")

    with open(path, "r") as f:
        wallpapers = [
            line.strip()
            for line in f.readlines()
            if line.strip()
        ]

    selected = random.choice(wallpapers)

    return os.path.join(
        WORKSHOP_DIR,
        selected
    )

def set_static_wallpaper(path):

    subprocess.run([
        "feh",
        "--bg-fill",
        path
    ])

def set_engine_wallpaper(path):

    subprocess.Popen([
        "linux-wallpaperengine",
        "--screen-root",
        DP_MONITOR,
        path
    ])

def main():

    colors = get_available_colors()

    if not colors:
        print("No hay colores compatibles.")
        return

    color = choose_color(colors)

    static_wp = random_static_wallpaper(color)
    engine_wp = random_engine_wallpaper(color)

    print(f"\nColor seleccionado: {color}")
    print(f"Static: {static_wp}")
    print(f"Engine: {engine_wp}")

    set_static_wallpaper(static_wp)
    set_engine_wallpaper(engine_wp)

if __name__ == "__main__":
    main()
