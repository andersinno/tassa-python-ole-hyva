# -*- coding: utf-8 -*-

class Timer:
    def __init__(self, name, total_time):
        self.name = name
        self.total_time = int(total_time)
        self.elapsed_time = 0

    def get_time_left(self):
        return max(self.total_time - self.elapsed_time, 0)
