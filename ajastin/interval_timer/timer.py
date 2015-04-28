# -*- coding: utf-8 -*-

class Timer:
    def __init__(self, name, total_time):
        self.name = name
        self.total_time = int(total_time)
        self.elapsed_time = 0

    def get_time_left(self):
        return max(self.total_time - self.elapsed_time, 0)

    def tick(self, seconds=1):
        self.elapsed_time += seconds

    def reset(self):
        self.elapsed_time = 0

    def to_json(self):
        return {
            "name": self.name,
            "total_time": self.total_time
        }

    @classmethod
    def from_json(cls, datum):
        return cls(**datum)

    def __eq__(self, other):
        # Note: elapsed_time is not tested by __eq__!
        return self.name == other.name and self.total_time == other.total_time
