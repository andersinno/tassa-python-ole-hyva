# -*- coding: utf-8 -*-
from interval_timer.ui.config_window import ConfigWindow


def test_config_window_makes_empty_timer_list():
    cw = ConfigWindow()
    # Window was never opened, never touched;
    # the timer list should have no entries
    # whatsoever.
    timer_list = cw.get_timer_list()
    assert not timer_list.timers
