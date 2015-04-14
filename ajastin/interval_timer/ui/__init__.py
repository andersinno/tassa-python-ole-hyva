# -*- coding: utf-8 -*-
from interval_timer.ui.config_window import ConfigWindow


def start_ui():
    config_window = ConfigWindow()
    config_window.open()
    timer_list = config_window.get_timer_list()
    # TODO: Start main window with configured timer list
