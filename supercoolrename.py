#!/usr/bin/env python3

import os
import os.path
import re

media_path = "/home/atlantis/torrents/completed"
media_dirs = os.listdir(media_path)

def rename():
    for medianame in media_dirs:
        media_formatted = re.sub('[^A-Za-z0-9]+', '.', medianame)
        os.rename (os.path.join(media_path, medianame),
                   os.path.join(media_path, media_formatted.rstrip('.').lower()))

if __name__ == '__main__':
    rename()
