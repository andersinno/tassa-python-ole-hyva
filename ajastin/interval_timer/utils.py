import os
import sys

SOUNDS_PATH = os.path.join(os.path.dirname(__file__), "sounds")

def play_sound(filename):
    if sys.platform == "win32":
        # On Windows, we can just use `winsound`
        import winsound
        winsound.PlaySound(filename, winsound.SND_ASYNC)
        return

    # On other platforms, let's guess at a suitable player...

    for player in [
        "/usr/bin/aplay",  # Linux (aplay)
        "/usr/bin/ffplay",  # Linux (ffmpeg)
        "/usr/bin/play",  # Linux (sox)
        "/usr/bin/afplay",  # OS X (Core Audio)
    ]:
        if os.path.isfile(player):
            os.system("%s '%s'" % (player, filename))
            return

    # Or do nothing at all :(

def play_sound_by_name(sound_name):
    play_sound(os.path.join(SOUNDS_PATH, sound_name))
