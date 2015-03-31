# -*- coding: utf-8 -*-
import random
import requests


def get_image_urls():
    response = requests.get("https://www.reddit.com/r/meow_irl/.json", headers={
        "User-Agent": "Furball"
    })
    json = response.json()
    images = []
    for child in json["data"]["children"]:
        url = child["data"]["url"]
        if "imgur" in url and (url.endswith(".jpg") or url.endswith(".jpeg")):
            images.append(url)
    return images


def download_random_cat_image():
    source_url = random.choice(get_image_urls())
    local_filename = "kuva.jpg"
    with open(local_filename, "wb") as file:
        response = requests.get(source_url)
        file.write(response.content)
    return local_filename


if __name__ == "__main__":
    download_random_cat_image()
