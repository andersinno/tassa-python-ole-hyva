import os
import sys

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

