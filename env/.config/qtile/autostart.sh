#!/bin/bash

# 2 monitors
# regular setup
xrandr --output "DP-4" --auto --primary --output "DP-3" --auto --left-of "DP-4"

# 3 monitors
# Reverse L-shape
# xrandr --output "DP-4" --pos 1920x0 --primary --output "DP-3" --pos 0x1080 --output "HDMI-0" --pos 0x0

redshift -l 41.6856872:-72.8092321 &
nitrogen --restore &
picom &
dunst &
lxpolkit &
