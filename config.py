from libqtile.config import Key, Screen, Group, Drag, Click
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


try:
    from typing import List  # noqa: F401
except ImportError:
    pass


color_alert = '#ee9900'


wps_logos = (('', {}),('', {}),('', {}),('', {}),('', {}))
wps_shortcuts = ('a','z','e','r','t')
groups = [Group(i, **kwargs) for i, kwargs in wps_logos]

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
	{'wmclass': 'confirmreset'},  # gitk     
	{'wmclass': 'makebranch'},  # gitk
	{'wmclass': 'maketag'},  #gitk     
	{'wname': 'branchdialog'},  # gitk     
	{'wname': 'pinentry'},  # GPG key password entry     
	{'wmclass': 'ssh-askpass'},  # ssh-askpass 
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"

bg_color = Colors()
default_fonts = DEFAULT_FONT

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    center_aligned=True,
                    padding=8,
                    borderwidth=2,
                    disable_drag=True,
                    rounded=False,
                    font="FontAwesome",
                    fontsize=16
                ),
                widget.Prompt(),
                widget.Spacer(length=15),
                widget.WindowName(
                    **default_fonts
                ),
#                widget.TextBox("default config", name="default"),
                widget.Systray(
                    icon_size=25
                ),
                widget.Spacer(length=15),
                Volume(
                    background=bg_color.get_next_color(),
                    **default_fonts
                ),
                Backlight(brightness_file="/sys/class/backlight/intel_backlight/actual_brightness",
                    max_brightness_file="/sys/class/backlight/intel_backlight/max_brightness",
                    **default_fonts,
                    background=bg_color.get_next_color()),
                Battery(charge_char=u'', 
                	discharge_char=u'', 
                	low_foreground=color_alert,
                	foreground="#ffffff",
                        background=bg_color.get_next_color(),
                        update_delay=2,
                        **default_fonts
                ),
                widget.Clock(
                    background=bg_color.get_next_color(),
                    **default_fonts
                ),
                widget.ThermalSensor(
                    background=bg_color.get_next_color(),
                    **default_fonts
                ),
                widget.CheckUpdates(
                    display_format='{updates}',
                    **default_fonts
                )
            ],
            35,
        ),
    ),
]

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
