#!/bin/sh

# Background
feh --bg-scale ~/Images/wallpaper/rain_girl.jpg &

# Tray apps
nm-applet &
blueman-applet &
caffeine &
pa-applet &
cbatticon &
pamac-tray &

# Stuff
xrdb -merge ~/.Xressources &
/home/benoit/bin/active_touch_pad &
compton -b


# Enable sudo auth popup
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & eval $(gnome-keyring-daemon -s --components=pkcs11,secrets,ssh,gpg) &
