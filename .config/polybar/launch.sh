#!/bin/bash 
# Terminate last polybar instance 

pkill -o polybar 

while pgred -u $UID -x polybar >/dev/null; do sleep 1; done 

polybar &

