# -- encoding: UTF-8 --

from interval_timer.timer import Timer


def test_timer_name_works():
    t = Timer("Syö pizzaa", 30)
    assert t.name == "Syö pizzaa"


def test_time_left_works():
    t = Timer("Syö pizzaa", 30)
    # No time has passed, so we should still have `total_time` seconds left
    assert t.get_time_left() == 30
    # Let's pass some time . . .
    t.elapsed_time += 5
    assert t.get_time_left() == 25
    # Let's elapse ALL THE TIME
    t.elapsed_time += 30
    assert t.get_time_left() == 0
