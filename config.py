from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from plasma import Plasma
import math
import os
import subprocess
from keys import keys
from helper import MOD, DEFAULT_FONT
from widget import Volume, Battery, Backlight
from colors_schemes import Colors
from screen import screen

try:
    from typing import List  # noqa: F401
except ImportError:
    pass


color_alert = '#ee9900'


# wps_logos = (('', {}),
#              ('', {}),
#              ('', {}),
#              ('', {}),
#              ('', {}))

wps_shortcuts = ('a','z','e','r','t')
#groups = [Group(i, **kwargs) for i, kwargs in wps_logos]

groups = [
    Group('', matches=[Match(wm_class=['google-chrome', 'Google-chrome'])]),
    Group('', matches=[Match(wm_class=['code', 'Code'])]),
    Group('', matches=[Match(wm_class=['spotify', 'Spotify'])]),
    Group(''),
    Group(''),
]

for a, i in enumerate(groups):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([MOD], wps_shortcuts[a], lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([MOD, "shift"], wps_shortcuts[a], lazy.window.togroup(i.name)),
])

layouts = [
    Plasma(
        border_normal='#333333',
        border_focus="#b5ded6",
        border_normal_fixed='#006863',
        border_focus_fixed='#00e8dc',
        border_width=2,
        border_width_single=1,
        margin=20
    )
]

widget_defaults = dict(
    font='FontAwesome',
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Drag floating layouts.
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  
 # type: List main = None
follow_mouse_focus = True 
bring_front_click = False 
cursor_warp = False
floating_layout = layout.Floating(float_rules=[     
	{'wmclass': 'confirm'},
	{'wmclass': 'dialog'},     
	{'wmclass': 'download'},     
	{'wmclass': 'error'},
	{'wmclass': 'file_progress'},     
	{'wmclass': 'notification'},     
	{'wmclass': 'splash'}, 
	{'wmclass': 'toolbar'},
    	{'wmclass': 'popup'},
    	{'wmclass': 'pop-up'},
    	{'wmclass': 'floating'},     
	{'wmclass': 'confirmreset'},  # gitk     
	{'wmclass': 'makebranch'},  # gitk
	{'wmclass': 'maketag'},  #gitk     
	{'wname': 'branchdialog'},  # gitk     
	{'wname': 'pinentry'},  # GPG key password entry     
	{'wmclass': 'ssh-askpass'},  # ssh-askpass
    
])
auto_fullscreen = True
focus_on_window_activation = "smart"
follow_mouse_focus = False

wmname = "LG3D"

default_fonts = DEFAULT_FONT



screens = [
    screen,
]

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
