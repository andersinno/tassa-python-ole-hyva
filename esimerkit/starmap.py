import random, os, time
import sys

width = 40
height = 30

while True:
    for row in range(height):
        print("".join(
            ("." if random.random() < 0.05 else " ")
            for col in range(width)
        ))
    time.sleep(0.1)

    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
