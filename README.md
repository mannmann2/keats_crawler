=============
Keats Crawler
=============

== Instructions

# Clone this repo
# `cd keats_crawler`
# `pip install -r requirements.txt`
# [Download chromedriver](https://chromedriver.chromium.org/downloads) for your version of Chrome
# `sudo apt install ffmpeg` (for Windows you'll need an alternative)
# Self enrol in module, if not already enrolled
# Update `keats_crawler/config.py` (Cookies must be updated each time your session expires)
# Run `crawl.py`


== Config settings

`MODULE`: Name of module and the folder in which to download files.
`URL`: Keats url for the module
`PATH`: Location in which to create the module folder
`PATH_TO_CHROMEDRIVER`: Location of chromedriver executable
`COOKIES`: Copy and add cookies from your browser after logging into Keats
`DOWNLOAD_VIDEOS`: True/False - Download videos embedded in Keats (Won't work for videos linked on some other website)
`DOWNLOAD_RESOURCES`: True/False - Download the non video resources (ppt, pdf, py, etc)
`SKIP_DUPLICATES`: True/False - To skip files already downloaded (Only works if the previous downloads occurred using this package)
`REMEMBER_DOWNLOADS`: True/False - Add files being downloaded in current crawl to a duplicate filter (Used to check duplicates)


* Free software: MIT license
