# -*- coding: utf-8 -*-
import codecs
import json

import os
from interval_timer.timer_list import TimerList

CONFIG_FILENAME = "interval_timer.json"

def get_config_path():
    """
    Get a writable path for saving configuration.
    If no path can be found, return None.

    :return: Path.
    :rtype: str|None
    """
    possible_paths = [
        os.environ.get("APPDATA"),  # Windows
        os.environ.get("XDG_CONFIG_HOME"),  # Linux
        os.path.expanduser("~/.config"),  # Fallback for Linux
        os.path.expanduser("~"),  # Fallback for other cases
        os.path.realpath("."),  # Really desperate now
    ]
    for path in possible_paths:
        if path and os.path.isdir(path) and os.access(path, os.W_OK):
            return path

def get_config_filename(access_flag=None):
    """
    Get the filename for the configuration file,
    if and only if it's accessible with the given
    access flag. (See the documentation for `os.access`
    for the available access flags.)

    :param access_flag: The access flag the file must be accessible with.
    :return: filename or none
    :rtype: str|None
    """
    path = get_config_path()
    if not path:
        return None
    filename = os.path.join(path, CONFIG_FILENAME)
    if access_flag and not os.access(filename, access_flag):
        return None
    return filename


def save_default_timer_list(timer_list):
    filename = get_config_filename(None)
    if not filename:  # No valid filename?
        return False  # Aww.
    with open(filename, "wb") as file:
        file.write(timer_list.to_json().encode("utf-8"))
    return True


def load_default_timer_list():
    """
    Load a default timer list.
    If the user has never used the program before,
    or they have deleted the configuration file,
    an empty list is returned.

    :return: A timer list, empty or not
    :rtype: TimerList
    """
    filename = get_config_filename(os.R_OK)
    if not filename:  # No filename?
        return TimerList()  # At least return something, then.

    with codecs.open(filename, "r", encoding="UTF-8") as file:
        json_data = json.load(file)  # Read JSON from the file
        return TimerList.from_json(json_data)
