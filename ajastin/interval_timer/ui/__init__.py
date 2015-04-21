# -*- coding: utf-8 -*-
from interval_timer.timer_list import TimerList
from interval_timer.ui.config_window import ConfigWindow
from interval_timer.ui.main_window import MainWindow


def start_ui():
    # TODO: Load user's last timer list
    last_timer_list = TimerList()
    config_window = ConfigWindow()
    config_window.initialize_from_timer_list(last_timer_list)
    config_window.open()
    timer_list = config_window.get_timer_list()
    # TODO: Save user's last timer list
    main_window = MainWindow(timer_list)
    main_window.open()
