# -*- coding: utf-8 -*-
import tkinter as tk

from PIL import ImageTk, Image

from furball import download_random_cat_image
from play_snd import play_sound

tk_image = None  # Need to use a global variable to hold a reference to the image


def greet_user():
    button1["bg"] = "orange"
    play_sound("terve.wav")


def get_new_image():
    global tk_image
    random_image_path = download_random_cat_image()
    image = Image.open(random_image_path)
    tk_image = ImageTk.PhotoImage(image)
    image_container["image"] = tk_image
    image_container.pack()
    play_sound("tuossa_kissa.wav")


def make_button(text, command, side):
    button = tk.Button(window, text=text, command=command)
    button.pack(side="top")
    return button


root = tk.Tk()
window = tk.Frame()
window.pack()
button1 = make_button("Terve", greet_user, "top")
button2 = make_button("Lataa kissa!", get_new_image, "top")
image_container = tk.Label(window)
window.mainloop()
