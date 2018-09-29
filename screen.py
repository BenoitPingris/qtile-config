from libqtile import bar, widget
from libqtile.config import Screen
from widget import Volume, Battery, Backlight
from colors_schemes import Colors
from helper import DEFAULT_FONT

bg_color = Colors()
color_alert = "#ee9900"
default_fonts = DEFAULT_FONT

screen = Screen(
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
            widget.Systray(
                icon_size=25,
                margin=15
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
                format=" %A %H:%M",
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
        35
    )
)

screen = Screen(
    top=bar.Bar(
        [
            widget.GroupBox(
                center_aligned=True,
                padding=6,
                borderwidth=2,
                disable_drag=True,
                rounded=False,
                font="FontAwesome",
                fontsize=16
            ),
            widget.WindowName(
                **default_fonts
            ),
            widget.Sep(height_percent=60),
            widget.Spacer(length=10),
            widget.Clock(
                format="%A %H:%M",
                font="FontAwesome",
                fontsize=15
            ),
            widget.Spacer(length=10),
            widget.Sep(height_percent=60),
            widget.Systray(icon_size=25,
                           padding=10),
            widget.Spacer(length=20)
        ],
        30
    )
)
