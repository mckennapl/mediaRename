# supercoolrename
A script I put together to rename media on my torrent server to make transferring to my NAS easier. Makes everything lowercase, replaces all non-alphanumeric characters (including spaces) with periods and strips anything not alphanumeric from either side of the name.

PleX compatible 😊.

## Usage
Change the `media_path` variable to your media directory. Then just run the script to rename everything.

## Notes
This is not recursive. I opted to not pursue that since I only use this script to make rsyncing easier. My reasoning to not to make this recursive is a fear that changing the media file within the media dir might make it harder for PleX to grab metadata.

I tried to leave out any sort of manual intervention so this could be run as a cron.
