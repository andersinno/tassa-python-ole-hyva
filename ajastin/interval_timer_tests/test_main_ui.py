# -*- coding: utf-8 -*-
from interval_timer.timer import Timer
from interval_timer.timer_list import TimerList
from interval_timer.ui.main_window import MainWindow


def _get_main_window():
    return MainWindow(timer_list=TimerList([
        Timer("dat pizza tho", 30),
        Timer("dat cola tho", 10),
    ]))


def test_main_window():
    mw = _get_main_window()
    first_timer = mw.timer_list.get_current_timer()
    time_left_1 = first_timer.get_time_left()
    mw.stop_command()
    mw.tick()
    # Stopped, so `tick` shouldn't do anything...
    assert first_timer.get_time_left() == time_left_1

    # Start! Tick! Go go go!
    mw.start_command()
    mw.tick()
    time_left_2 = first_timer.get_time_left()
    assert time_left_2 < time_left_1

    # Since there are two timers in the list,
    # calling `next_command` twice should wrap
    # us back to the first timer.
    mw.next_command()
    mw.next_command()
    assert mw.timer_list.get_current_timer() == first_timer
    mw.next_command()
    assert mw.timer_list.get_current_timer() != first_timer
    mw.reset_command()
    assert mw.timer_list.get_current_timer() == first_timer

