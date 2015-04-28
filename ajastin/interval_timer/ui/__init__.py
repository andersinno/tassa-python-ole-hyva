# -*- coding: utf-8 -*-
from interval_timer.prefs import load_default_timer_list, save_default_timer_list
from interval_timer.ui.config_window import ConfigWindow
from interval_timer.ui.main_window import MainWindow
try:
    import tkinter.messagebox as mb
except ImportError:  # pragma: no cover
    # Python 2.x?
    import tkMessageBox as mb

def start_ui():
    last_timer_list = load_default_timer_list()
    config_window = ConfigWindow()
    config_window.initialize_from_timer_list(last_timer_list)
    config_window.open()
    timer_list = config_window.get_timer_list()
    if not timer_list.timers:
        return

    try:
        save_default_timer_list(timer_list)
    except Exception as exc:
        mb.showwarning("Unable to save timer list", exc)

    main_window = MainWindow(timer_list)
    main_window.open()
