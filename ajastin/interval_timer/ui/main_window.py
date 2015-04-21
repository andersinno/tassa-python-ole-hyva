# -*- coding: utf-8 -*-

import tkinter as tk

from interval_timer.utils import play_sound_by_name


TIMER_SPEED = 100

try:
    import tkinter.messagebox as mb
except ImportError:  # Python 2.x?
    import tkMessageBox as mb


def gridify(widget, **grid_kwargs):
    widget.grid(**grid_kwargs)
    return widget


class MainWindow(object):
    def create_ui(self):
        self.frame = tk.Frame()
        self.time_label = gridify(
            tk.Label(self.frame, font="Arial 48"),
            row=0, column=0, columnspan=4, padx=130, pady=30
        )
        self.name_label = gridify(
            tk.Label(self.frame, font="Arial 36"),
            row=1, column=0, columnspan=4, pady=15
        )
        button_attrs = {
            "padx": 10,
            "pady": 10,
            "font": "Arial 24"
        }
        button_grid_attrs = {
            "padx": 30,
            "pady": 30
        }
        self.start_button = gridify(
            tk.Button(self.frame, text="Start", command=self.start_command, **button_attrs),
            row=2, column=0, **button_grid_attrs
        )
        self.stop_button = gridify(
            tk.Button(self.frame, text="Stop", command=self.stop_command, **button_attrs),
            row=2, column=1, **button_grid_attrs
        )
        self.next_button = gridify(
            tk.Button(self.frame, text="Next", command=self.next_command, **button_attrs),
            row=2, column=2, **button_grid_attrs
        )
        self.reset_button = gridify(
            tk.Button(self.frame, text="Reset", command=self.reset_command, **button_attrs),
            row=2, column=3, **button_grid_attrs
        )
        self.frame.pack()

    def __init__(self, timer_list):
        self.timer_list = timer_list
        self.timer_active = False
        self.create_ui()
        self.update_labels()
        self.frame.after(TIMER_SPEED, self.tick)

    def tick(self):
        self.frame.after(TIMER_SPEED, self.tick)
        if self.timer_active:
            current_timer = self.timer_list.get_current_timer()
            current_timer.tick()
            if current_timer.get_time_left() <= 0:
                if self.timer_list.is_current_last_timer():
                    play_sound_by_name("finish.wav")
                else:
                    play_sound_by_name("single_timer.wav")

                current_timer.reset()
                self.timer_list.select_next_timer()
            self.update_labels()

    def update_labels(self):
        current_timer = self.timer_list.get_current_timer()
        self.name_label["text"] = current_timer.name
        time_left_seconds = current_timer.get_time_left()
        time_left_text = "{:02d}:{:02d}:{:02d}".format(
            int(time_left_seconds / 60 / 60),
            int((time_left_seconds / 60) % 60),
            int(time_left_seconds % 60),
        )
        self.time_label["text"] = time_left_text

    def start_command(self):
        self.timer_active = True

    def stop_command(self):
        self.timer_active = False

    def next_command(self):
        self.timer_list.select_next_timer()
        self.timer_list.get_current_timer().reset()
        self.update_labels()

    def reset_command(self):
        self.timer_active = False
        self.timer_list.reset()
        self.update_labels()

    def open(self):
        """
        Open the main window.

        This call will block until the user has finished with their interval training.
        """
        self.frame.mainloop()
