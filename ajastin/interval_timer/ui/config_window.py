# -*- coding: utf-8 -*-

import tkinter as tk
from interval_timer.timer import Timer
from interval_timer.timer_list import TimerList

try:
    import tkinter.messagebox as mb
except ImportError:  # pragma: no cover
    # Python 2.x?
    import tkMessageBox as mb

class ConfigWindow(object):
    def __init__(self):
        self.timer_list = TimerList()
        self.frame = tk.Frame()
        tk.Label(self.frame, text="Timer Name").grid(row=0, column=0)
        tk.Label(self.frame, text="Timer Duration", justify="right").grid(row=0, column=1)
        tk.Button(self.frame, text="OK", command=self.make_timers_and_close).grid(row=11, column=0, columnspan=2, pady=10)
        self.build_inputs()
        self.frame.pack()

    def build_inputs(self):
        entry_field_margin_x = 15
        entry_field_margin_y = 7
        self.inputs = []

        for x in range(10):
            grid_row = x + 1
            timer_name_entry = tk.Entry(self.frame)
            timer_name_entry.grid(row=grid_row, column=0, padx=entry_field_margin_x, pady=entry_field_margin_y)
            timer_time_entry = tk.Entry(self.frame, justify="right")
            timer_time_entry.grid(row=grid_row, column=1, padx=entry_field_margin_x, pady=entry_field_margin_y)
            self.inputs.append((timer_name_entry, timer_time_entry))

    def open(self):
        """
        Open the configuration window.

        This call will block until the user has finished configuring things.
        """
        self.frame.mainloop()

    def construct_timer_list(self):
        """
        Read the configuration from the user's inputs and create a TimerList instance.
        """
        timers = []
        for (name_entry, time_entry) in self.inputs:
            name = name_entry.get()
            time_text = time_entry.get()
            if not (name and time_text):
                continue
            seconds = int(time_text)
            timers.append(Timer(name=name, total_time=seconds))
        timer_list = TimerList(timers)
        return timer_list

    def make_timers_and_close(self):
        """
        Read the configuration from the user's inputs, create a TimerList instance and close this window.
        """

        timer_list = self.construct_timer_list()

        if not timer_list.timers:
            mb.showerror(message="No timers.")
            return


        self.timer_list = timer_list
        self.frame.destroy()
        self.frame.quit()

    def get_timer_list(self):
        """
        Get the TimerList that the user configured with this window.

        :return: A timer list.
        :rtype: TimerList
        """
        return self.timer_list

    def initialize_from_timer_list(self, timer_list):
        for i, timer in enumerate(timer_list.timers[:10]):
            self.inputs[i][0].insert(0, timer.name)
            self.inputs[i][1].insert(0, timer.total_time)
