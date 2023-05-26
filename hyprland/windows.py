import json
import subprocess
import logging
from hyprland.util import get_child_or_else

logger = logging.getLogger(__name__)

def focus(con):
    logger.error('foo')
    con_address = con['address']
    logger.error(con_address)

    subprocess.check_output(["hyprctl", "dispatch", "focuswindow", f"address:{con_address}"])


def get_windows():
    windows = json.loads(subprocess.check_output(["hyprctl", "clients", "-j"]))
    active_address = json.loads(subprocess.check_output(["hyprctl", "activewindow", "-j"]))['address']
    for w in windows:
        w['active'] = w['address'] == active_address
    return windows


def app_details(con):
    # (con_id, application name, window title)
    return (con["address"], con["initialTitle"], con["title"])


if __name__ == "__main__":
    clients = get_clients()
    wins = get_windows(clients)

    for w in wins:
        print(app_details(w))
