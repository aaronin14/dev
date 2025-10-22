#
#                         ____             _       _ _  _
#              __ _  __ _|  _ \ ___  _ __ (_)_ __ / | || |
#             / _` |/ _` | |_) / _ \| '_ \| | '_ \| | || |_
#            | (_| | (_| |  _ < (_) | | | | | | | | |__   _|
#             \__,_|\__,_|_| \_\___/|_| |_|_|_| |_|_|  |_|
#
#   Personal Qtile configuration of aaRonin14 <aaron14nguyen@gmail.com>
#  --------------------------------------------------------------------

# Imports
import os
import subprocess
from libqtile import hook, widget, bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import colors

# Variables
mod = "mod4"  # Mod Key is SUPER
home = os.path.expanduser("~")  # Allow using 'home +' to expand ~
terminal = "kitty"
webBrowser= "firefox"
appLauncher = "rofi -show drun"
noteTaking = "obsidian"
todoist = "todoist"
powerScript = f"rofi -show power-menu -modi power-menu:{home}/.config/rofi/scripts/rofi-power-menu -config {home}/.config/rofi/themes/config_power_kanagawa.rasi"

# Unminimize games
@lazy.group.function
def unminimize_all(group):
    for win in group.windows:
        if win.minimized:
            win.toggle_minimize()

# Keybindings
keys = [
    # Launch/Kill Stuffs
    Key([mod], "Return", lazy.spawn(appLauncher), desc="Lauch rofi"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "w", lazy.spawn(webBrowser), desc="Lauch Web Browser"),
    Key([mod], "e", lazy.spawn(noteTaking), desc="Launch Note Taking App"),
    Key([mod], "r", lazy.spawncmd(), desc="Run Command"),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "u", lazy.spawn(todoist), desc="Launch Todoist"),
    Key([mod], "Escape", lazy.spawn(powerScript), desc="Launch Power Menu"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    #Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Control Brightness, Volume
    Key([], "XF86MonBrightnessUp", lazy.spawn(home + "/.config/dunst/scripts/backlight.sh up"), desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown",lazy.spawn(home + "/.config/dunst/scripts/backlight.sh down"), desc="Decrease brightness"),
    Key([], "XF86AudioMute", lazy.spawn(home + "/.config/dunst/scripts/volume.sh mute"), desc="Mute Volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(home + "/.config/dunst/scripts/volume.sh up"), desc="Raise Volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(home + "/.config/dunst/scripts/volume.sh down"), desc="Lower Volume"),
    # Switch Screen
    Key([mod], "p", lazy.next_screen()),
    Key([mod], "o", lazy.prev_screen()),
    # Screenshots
    Key([mod, "shift"], "S", lazy.spawn("flameshot gui")),
    Key([], "Print", lazy.spawn("flameshot screen")),
    Key([mod], "Print", lazy.spawn("flameshot full")),
    # Switch between windows
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "control"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    # Toggle between different layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod, "shift"], "m", unminimize_all, desc="Unminimize all windows in current group"),
]

# Setting Up Groups / Workspace
groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
group_labels = ["一", "二", "三", "四", "五", "六", "七", "八", "九"]
#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#group_labels = ["một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
group_layouts = ["columns", "columns", "columns", "columns", "columns", "columns", "columns", "columns", "floating"]
group_matches = [
    [ #1
        Match(wm_class="firefox")
    ],
    [ #2
        Match(wm_class="kitty")
    ],
    [ #3
        Match(wm_class="obsidian")
    ],
    [ #4
        Match(wm_class="code-oss"),
        Match(wm_class="jetbrains-idea-ce"),
        Match(wm_class="Godot"),
        Match(wm_class="Godot_editor"),
    ],
    [ #5
    ],
    [ #6
        Match(wm_class="steam")
    ],
    [ #7
        Match(wm_class="Todoist")
    ],
    [ #8
        Match(wm_class="discord"),
        Match(wm_class="slack"),
        Match(wm_class="spotify"),
        Match(wm_class="zoom")
    ],
    [ #9
        Match(wm_class="lxappearance"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="pwvucontrol"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="nm-connection-editor"),
        Match(wm_class="lxappearance"),
    ]
]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
            layout=group_layouts[i],
            matches=group_matches[i],
        )
    )

# Movement between Workspace
for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc="move focused window to group {}".format(i.name)),
        ]
    )


# Layouts Settings
colors = colors.kanagawa_dragon
layout_theme= {
    "border_normal":colors["bg"],
    "border_focus":colors["blue"],
    "border_width":2,
    "margin":2,
}
layouts = [
    layout.Columns(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme),
]


# Widget Default Settings
widget_defaults = dict(
    font="Mononoki Nerd Font",
    fontsize=12,
    padding=4,
    background=colors["bg"],
)
extension_defaults = widget_defaults.copy()

def longNameParse(text):
    for string in ["Chromium", "Firefox", "Brave"]:
        if string in text:
            text = string
        else:
            text = text
    return text

def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            active=colors["fg"],
            inactive=colors["light_black"],
            highlight_method="line",
            highlight_color=colors["yellow"],
            block_highlight_text_color=colors["light_white"],
            borderwidth=0,
            disable_drag=True,
        ),
        widget.Sep(
            foreground=colors["yellow"],
        ),
        widget.CurrentLayoutIcon(
            foreground=colors["fg"],
            scale=0.75,
            fmt="{}",
        ),
        widget.Sep(
            foreground=colors["yellow"],
        ),
        widget.WindowName(
            parse_text=longNameParse,
            format="{name}",
            foreground=colors["yellow"],
            empty_group_string="Desktop",
        ),
        widget.Sep(
            foreground=colors["yellow"],
        ),
        widget.Systray(
            fontsize=2,
        ),
        widget.Volume(
            emoji=True,
            emoji_list=["󰝟 "," "," "," "],
            foreground=colors["fg"],
        ),
        widget.Sep(
            foreground=colors["yellow"],
        ),
        widget.CPU(
            foreground=colors["fg"],
            format="{load_percent}%",
            fmt="CPU {}",
        ),
        widget.Sep(
            foreground=colors["yellow"],
        ),
        widget.Memory(
            foreground=colors["fg"],
            format="{MemUsed:.1f}{mm}",
            fmt="MEM {}",
            mouse_callbacks={"Button1": lazy.spawn(terminal + " -e htop")},
            update_interval="5",
        ),
        widget.Sep(
            foreground=colors["yellow"],
        ),
        widget.ThermalSensor(
            threshold=30,
            foreground=colors["fg"],
            fmt="TEMP {}",
        ),
        widget.Sep(
            foreground=colors["yellow"],
        ),
        widget.Battery(
            foreground=colors["fg"],
        ),
        widget.Sep(
            foreground=colors["yellow"],
        ),
        widget.Clock(
            foreground=colors["fg"],
            format="%Y-%m-%d %I:%M",
            mouse_callbacks={
                "Button1": lazy.spawn(webBrowser + " https://calendar.google.com/u/0")
            },
        ),
        widget.Spacer(
            length=2,
        ),
    ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1
#def init_widgets_screen2():
#    widgets_screen2 = init_widgets_list()
#    del widgets_screen2[6:-2]
#    return widgets_screen2
#def init_widgets_screen3():
#    widgets_screen3 = init_widgets_list()
#    del widgets_screen3[6:-2]
#    return widgets_screen3

def init_screens():
    return [Screen(bottom=bar.Bar(widgets=init_widgets_screen1(),
                               background=colors["black"],
                               size=20,
                               border_color=colors["blue"],
                               border_width=0,
                               margin=[0,0,0,0],)),
#            Screen(bottom=bar.Bar(widgets=init_widgets_screen2(),
#                               background=colors["black"],
#                               size=20,
#                               border_color=colors["blue"],
#                               border_width=0,
#                               margin=[0,0,0,0],)),
#            Screen(bottom=bar.Bar(widgets=init_widgets_screen3(),
#                               background=colors["black"],
#                               size=20,
#                               border_color=colors["blue"],
#                               border_width=0,
#                               margin=[0,0,0,0],))
            ]
if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
#    widgets_screen2 = init_widgets_screen2()
#    widgets_screen3 = init_widgets_screen3()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod, "control"], "Button1", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button3", lazy.window.bring_to_front()),
    Click([mod], "Button2", lazy.window.toggle_floating()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])
