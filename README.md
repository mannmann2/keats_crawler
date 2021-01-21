# Keats Crawler

### Instructions

1. Clone this repo
1. `cd keats_crawler`
1. `pip install -r requirements.txt`
1. [Download chromedriver](https://chromedriver.chromium.org/downloads) for your version of Chrome
1. `sudo apt install ffmpeg` (for Windows you'll need an alternative)
1. Self enrol in the Keats module, if not already enrolled
1. Update `config.py` (Cookies must be updated each time your session expires)
1. Run: `python crawl.py`


### Config settings

`MODULE`: Name of module and the folder in which to download files.
`URL`: Keats url for the module
`PATH`: Location in which to create the module folder
`PATH_TO_CHROMEDRIVER`: Location of chromedriver executable
`COOKIES`: Copy and add cookies from your browser after logging into Keats
`DOWNLOAD_VIDEOS`: True/False - Download videos embedded in Keats (Won't work for videos linked on some other website)
`DOWNLOAD_RESOURCES`: True/False - Download the non-video resources (ppt, pdf, py, etc)
`SKIP_DUPLICATES`: True/False - To skip files already downloaded (Only works if the previous downloads occurred using this package)
`REMEMBER_DOWNLOADS`: True/False - Add files being downloaded in current crawl to a duplicate filter (Used to check duplicates)


* Free software: MIT license
