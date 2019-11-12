#!/usr/bin/env python3
"""Renames the contents of a directory to replace all non-alphanum characters
(including spaces) with periods. Also strips any trailing periods off of the
filename. Ex. "A New DVD [2019] (1080p)" becomes "a.new.dvd.2019.1080p"

This is PLeX compliant.

Usage:
    Just run it from the commandline: Ex. "./supercoolrename.py"
    Also feel free to change the dir_path variable if you'd like to run it from
    a different location on your machine. You will most likely need to add additional logic to make that work.
"""

import os
import re

dir_path = os.getcwd()
media_path = os.listdir(dir_path)

print ("") #This is to add readibility to the first filename block


def rename():
    """First prints filename before change is applied, replaces all
    non-alphanumeric characters and spaces with periods, forces filename to be
    lowercase, and then prints out changed name.

    Returns:
        Both unchanged and changed filenames in a blocked out list.
    """
    for medianame in media_path:
        print(medianame + " was renamed to:")
        media_formatted = re.sub('[^A-Za-z0-9]+', '.', medianame)
        os.rename(medianame, media_formatted.rstrip('.').lower())
        print(media_formatted.rstrip('.').lower()) #will
        print("")


def success():
    """Returns a success message when everything is successfully renamed.

    Returns:
        A success message when everything is successfully renamed.
    """
    print("Success. Media directory naming scheme compliant.")


if __name__ == '__main__':
    rename()
    success()
