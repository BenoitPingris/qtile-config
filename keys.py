from libqtile.command import lazy
from libqtile.config import Key
from helper import MOD, SPACE

keys = [
    # Switch window focus to other pane(s) of stack                                      
    Key([MOD], "space", lazy.layout.next()),
    Key([MOD], "Return", lazy.spawn("termite")),
    # Toggle between different layouts as defined below                                  
    Key([MOD], "Tab", lazy.next_layout()),
    Key([MOD], "w", lazy.window.kill()),
    Key([MOD, "control"], "r", lazy.restart()),
    Key([MOD, "control"], "q", lazy.shutdown()),
    Key([MOD], "d", lazy.spawn("rofi -show drun")),
    Key([MOD], "Left", lazy.layout.left()),
    Key([MOD], "Right", lazy.layout.right()),
    Key([MOD], "Up", lazy.layout.up()),
    Key([MOD], "Down", lazy.layout.down()),
    Key([MOD], "f", lazy.window.toggle_fullscreen()),
    Key([MOD, "shift"], "space", lazy.window.toggle_floating()),
    Key([], 'XF86AudioMute', lazy.spawn('amixer -q sset Master toggle')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer -q sset Master 5%+')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer -q sset Master 5%-')),
    Key([], 'XF86MonBrightnessUp', lazy.spawn('xbacklight -inc 10')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('xbacklight -dec 10')),
    Key([MOD], 'v', lazy.layout.mode_vertical()),
    Key([MOD], 'h', lazy.layout.mode_horizontal()),
    Key([MOD, "shift"], 'Left', lazy.layout.grow_width(SPACE)),
    Key([MOD, "shift"], 'Right', lazy.layout.grow_width(-SPACE)),
    Key([MOD, "shift"], 'Up', lazy.layout.grow_height(SPACE)),
    Key([MOD, "shift"], 'Down', lazy.layout.grow_height(-SPACE)),
    Key([MOD, "control"], "Left", lazy.layout.move_left()),
    Key([MOD, "control"], "Right", lazy.layout.move_right()),
    Key([MOD, "control"], "Up", lazy.layout.move_up()),
    Key([MOD, "control"], "Down", lazy.layout.move_down()),
    Key([MOD, "shift"], "l", lazy.spawn('dm-tool lock')),
    Key([MOD, "shift"], "k", lazy.spawn('/home/benoit/bin/lock_suspend'))
]
