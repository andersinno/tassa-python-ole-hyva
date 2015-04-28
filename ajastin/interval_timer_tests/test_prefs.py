# -*- coding: utf-8 -*-
import os
import uuid

from interval_timer import prefs
from interval_timer.timer import Timer
from interval_timer.timer_list import TimerList


def test_xxget_config_path():
    assert prefs.get_config_path()  # We get something out of it?
    app_data = os.environ.pop("APPDATA", None)  # Remove appdata (for Windows) if it exists
    try:
        assert prefs.get_config_path()  # We get a fallback?
    finally:
        if app_data:  # Put it back if we need to
            os.environ["APPDATA"] = app_data


def test_save_load_config():
    test_config_filename = "%s.json" % uuid.uuid4()
    original_config_filename = prefs.CONFIG_FILENAME
    try:
        prefs.CONFIG_FILENAME = test_config_filename
        t = TimerList([
            Timer("Töttöröö", 10),
            Timer("Tetteree", 20),
            Timer("Tattaraa", 30),
        ])
        prefs.save_default_timer_list(t)
        assert os.path.isfile(prefs.get_config_filename())
        t2 = prefs.load_default_timer_list()
        assert t.timers == t2.timers
        os.remove(prefs.get_config_filename())
    finally:
        prefs.CONFIG_FILENAME = original_config_filename
