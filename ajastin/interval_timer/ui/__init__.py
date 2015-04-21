# -*- coding: utf-8 -*-
from interval_timer.ui.config_window import ConfigWindow
from interval_timer.ui.main_window import MainWindow


def start_ui():
    config_window = ConfigWindow()
    config_window.open()
    timer_list = config_window.get_timer_list()
    main_window = MainWindow(timer_list)
    main_window.open()
