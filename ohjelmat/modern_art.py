# -*- coding: utf-8 -*-
import random
from PIL import Image, ImageDraw
import math
import argparse

BUILTIN_PALETTES = [
    [[255, 78, 80], [252, 145, 58], [249, 212, 35], [237, 229, 116], [225, 245, 196]],
    [[253, 230, 189], [161, 197, 171], [244, 221, 81], [209, 30, 72], [99, 47, 83]],
    [[204,38,73],[153,44,75],[102,50,76],[51,56,78],[0,62,79]],
    [[246,227,171],[180,63,90],[75,29,55],[112,87,91],[134,155,136]]
]

def get_palettes():
    import requests
    palettes = []
    for palette in requests.get("http://www.colourlovers.com/api/palettes/top?format=json").json():
        hex_colors = palette["colors"]  # List of the form ["FFAAFF", "003344", ...]
        colors = [
            # Convert "FFCCFF" to (255, 204, 255)
            (int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:], 16))
            for hex
            in hex_colors
        ]
        palettes.append(colors)
    return palettes

class PointInfo(object):
    def __init__(self, x, y, h, lx=0):
        self.x = x
        self.y = y
        self.h = h
        self.lx = lx


class DrawStrategy(object):
    def get_point_info(self, i):
        """
        :param i: Point index (0..1)
        :type i: float
        :rtype: PointInfo
        """
        raise NotImplementedError("Not implemented")

    def get_n_points(self):
        return 5

class SineStripeDrawer(DrawStrategy):
    def __init__(self):
        self.phase = random.random()
        self.center = random.random()

    def get_point_info(self, i):
        return PointInfo(
            i,
            self.center + math.sin((i + self.phase) * 6.283) * 0.02,
            0.01
        )

    def get_n_points(self):
        return 150

class RandomStripeDrawer(DrawStrategy):
    def get_point_info(self, i):
        return PointInfo(
            x=i,
            y=random.uniform(0.4, 0.6),
            h=random.uniform(0.01, 0.03),
        )


def draw_stripe(image, palette, strategy):
    draw = ImageDraw.Draw(image)
    upper_points = []
    lower_points = []
    n_points = strategy.get_n_points()
    for p in range(n_points + 1):
        point_info = strategy.get_point_info(p / float(n_points))
        upper_points.append((point_info.x, point_info.y - point_info.h))
        lower_points.append((point_info.x + point_info.lx, point_info.y + point_info.h))

    points = lower_points + upper_points[::-1]

    width, height = image.size

    pixel_points = [
        (x * width, y * height)
        for (x, y)
        in points
    ]

    draw.polygon(pixel_points, fill=random.choice(palette))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--interwebs", action="store_true", default=False)
    args = ap.parse_args()
    if args.interwebs:
        palettes = get_palettes()
    else:
        palettes = BUILTIN_PALETTES
    palette = [tuple(rgb) for rgb in random.choice(palettes)]
    image = Image.new("RGB", (4096, 2160))
    image.paste(random.choice(palette))

    strategy_class = random.choice([
        SineStripeDrawer,
        RandomStripeDrawer
    ])

    for x in range(10):
        strategy = strategy_class()
        draw_stripe(image, palette, strategy)

    image = image.resize((1920, 1200), Image.ANTIALIAS)

    image.show()

if __name__ == "__main__":
    main()
