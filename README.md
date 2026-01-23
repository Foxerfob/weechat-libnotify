# WeeChat notify-send plugin

Minimalistic desktop notifications for WeeChat using `notify-send`.

## Features
- Desktop notifications for incoming messages
- Toggle on/off with command
- Shows server/channel in notification title
- Format: `nick: message`
- Ignores your own messages

## Installation
```bash
# Copy to WeeChat plugins directory
cd ~/.weechat/python/ # or ~/.local/share/weechat/python/ depends on your WeeChat version and configuration.
wget -O notify_send.py https://github.com/Foxerfob/weechat-libnotify/raw/refs/heads/main/notify_send.py
# For auto-load on startup:
cd autoload
ln -s ../notify_send.py
```

## Usage
- Notifications are enabled by default
- Toggle: `/notify_toggle [on|off]`
- Show status: `/notify_status`
- Without argument: `/notify_toggle` toggles state

## Requirements
- WeeChat with Python support
- `notify-send` command (usually from `libnotify-bin` package)

## License
Distributed under the GPLv3 license. See the LICENSE file for more details.
