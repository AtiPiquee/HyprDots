#!/bin/sh

IMAGE_PATH="$1"

if ! pgrep -x "swww-daemon" > /dev/null; then
    swww-daemon & 
    sleep 1
fi

swww img -o eDP-1 \
    --transition-type wipe \
    --transition-angle 30 \
    --transition-step 90 \
    "$IMAGE_PATH"