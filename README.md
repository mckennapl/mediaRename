# supercoolrename
A script I put together to rename media on my torrent server to make
transferring to my NAS easier. Makes everything lowercase, replaces all
non-alphanumeric characters (including spaces) with periods and strips anything
not alphanumeric from either side of the name.

PleX compatible 😊

## Usage
Move `supercoolrename.py` to your media directory, make sure the permissions are
correct `chmod +x supercoolrename.py`, and run it `./supercoolrename`!

OR set it as an alias and rename everything in your current working directory.

For example
``` bash
alias rename="/home/user/git/supercoolrename/supercoolrename.py"
```

## Disclaimer
There are no guard rails on this and it *will* rename everything in the current
working directory without prompting. Use at your own risk!

## Notes
This is not recursive. I opted to not pursue that since I only use this script
to make rsyncing easier, and a fear that changing the media file within the
media dir might make it harder for PleX to grab metadata.

I tried to leave out any sort of manual intervention so this could be run as a
cron.
