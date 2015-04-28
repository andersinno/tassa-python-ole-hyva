# -*- coding: utf-8 -*-
import json
from interval_timer.timer import Timer


class TimerList:
    def __init__(self, timers=()):
        self.timers = []
        self.timers.extend(timers)
        self.current_timer_index = 0

    def get_current_timer(self):
        return self.timers[self.current_timer_index]

    def select_next_timer(self):
        self.current_timer_index = (self.current_timer_index + 1) % len(self.timers)

    def reset(self):
        for timer in self.timers:
            timer.reset()
        self.current_timer_index = 0

    def is_current_last_timer(self):
        return self.current_timer_index == len(self.timers) - 1

    def to_json(self):
        return json.dumps([t.to_json() for t in self.timers], ensure_ascii=False)

    @classmethod
    def from_json(cls, json_data):
        timers = [Timer.from_json(datum) for datum in json_data]
        return cls(timers=timers)
