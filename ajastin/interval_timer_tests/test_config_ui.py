# -*- coding: utf-8 -*-
from interval_timer.ui.config_window import ConfigWindow


def test_config_window_makes_empty_timer_list():
    cw = ConfigWindow()
    # Window was never opened, never touched;
    # the timer list should have no entries
    # whatsoever.
    timer_list = cw.get_timer_list()
    assert not timer_list.timers


def test_config_window_makes_good_timer_list():
    cw = ConfigWindow()
    cw.inputs[0][0].insert(0, "Test")
    cw.inputs[0][1].insert(0, "60")
    cw.make_timers_and_close()
    timer_list = cw.get_timer_list()
    assert timer_list.timers[0].get_time_left() == 60

