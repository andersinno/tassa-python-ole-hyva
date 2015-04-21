# -*- coding: utf-8 -*-

class TimerList:
    def __init__(self, timers=()):
        self.timers = []
        self.timers.extend(timers)
        self.current_timer_index = 0

    # TODO: Implement the rest of this object according to spec.
