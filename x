. Script launcher para i3wm

Guárdalo como:

~/Scripts/run_sync_wallpapers.sh

Código:

#!/bin/bash

python ~/Scripts/sync_wallpapers.py
Permisos
chmod +x ~/Scripts/*.sh
chmod +x ~/Scripts/*.py
Instalar
~/Scripts/setup_sync_wallpapers.sh
Ejecutar

Manual:

python ~/Scripts/sync_wallpapers.py

o automático:

python ~/Scripts/random_sync_wallpapers.py
Integración con i3wm

Agrega en:

~/.config/i3/config

esto:

bindsym $mod+Shift+s exec ~/Scripts/run_sync_wallpapers.sh

Luego:

i3-msg reload
Funcionamiento

Ejemplo:

Colores disponibles:

1. blue
2. purple
3. red
4. black

Selecciona un color:

Luego:

monitor HDMI-A-1 → wallpaper estático con feh
monitor DP-1 → wallpaper animado con linux-wallpaperengine

Ambos del mismo color base.
