#!/usr/bin/env python3

import os
import re

dir_path = os.getcwd()
media_path = os.listdir(dir_path)

def rename():
    for medianame in media_path:
        media_formatted = re.sub('[^A-Za-z0-9]+', '.', medianame)
        os.rename(medianame, media_formatted.rstrip('.').lower())

def success():
    print("Media directory naming scheme compliant")


if __name__ == '__main__':
    rename()
    success()
