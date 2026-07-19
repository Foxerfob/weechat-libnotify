#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# notify-send plugin for WeeChat
# Minimalistic notifications with toggle command

import weechat
import subprocess
import html

SCRIPT_NAME = "notify_send"
SCRIPT_AUTHOR = "Foxerfob"
SCRIPT_VERSION = "0.2"
SCRIPT_LICENSE = "GPL3"
SCRIPT_DESC = "Desktop notifications with toggle"

notify_enabled = True


def sanitize_text(text = ""):
    escaped_slashes = text.replace('\\', '\\\\')
    return html.escape(escaped_slashes)


def notify_send(server_channel, nick, message):
    try:
        server_channel = sanitize_text(server_channel)
        nick = sanitize_text(nick) 
        message = sanitize_text(message)

        title = f"WeeChat - {server_channel}"
        body = f"{nick}: {message}"
        subprocess.run(["notify-send", "-e", title, body], check=False)
    except Exception as e:
        weechat.prnt("", f"notify-send error: {e}")


def msg_cb(data, buffer, date, tags, displayed, highlight, prefix, message):
    global notify_enabled

    if not notify_enabled:
        return weechat.WEECHAT_RC_OK

    if "notify_none" in tags or "self_msg" in tags:
        return weechat.WEECHAT_RC_OK

    buffer_name = weechat.buffer_get_string(buffer, "name")
    notify_send(buffer_name, prefix, message)
    return weechat.WEECHAT_RC_OK


def toggle_cmd_cb(data, buffer, args):
    global notify_enabled

    if args == "":
        notify_enabled = not notify_enabled
    elif args == "on":
        notify_enabled = True
    elif args == "off":
        notify_enabled = False
    else:
        weechat.prnt(buffer, "Usage: /notify_toggle [on|off]")
        weechat.prnt(buffer, "  no argument: toggle current state")
        return weechat.WEECHAT_RC_ERROR

    status = "enabled" if notify_enabled else "disabled"
    weechat.prnt(buffer, f"notify-send: notifications {status}")
    return weechat.WEECHAT_RC_OK


def status_cmd_cb(data, buffer, args):
    global notify_enabled
    status = "enabled" if notify_enabled else "disabled"
    weechat.prnt(buffer, f"notify-send: notifications are {status}")
    return weechat.WEECHAT_RC_OK


if __name__ == "__main__":
    if weechat.register(
        SCRIPT_NAME,
        SCRIPT_AUTHOR,
        SCRIPT_VERSION,
        SCRIPT_LICENSE,
        SCRIPT_DESC,
        "",
        ""
    ):
        # Hook for private messages and channel messages
        weechat.hook_print("", "irc_privmsg", "", 1, "msg_cb", "")

        # Command to toggle notifications
        weechat.hook_command(
            "notify_toggle",
            "Toggle desktop notifications",
            "[on|off]",
            "on: enable notifications\noff: disable notifications\n"
            "(no argument): toggle current state",
            "on||off",
            "toggle_cmd_cb",
            ""
        )

        # Command to show status
        weechat.hook_command(
            "notify_status",
            "Show notifications status",
            "",
            "",
            "",
            "status_cmd_cb",
            ""
        )

        weechat.prnt(
            "", "notify-send plugin loaded. Use /notify_toggle to control.")

