# Keats Crawler

This is a python module for downloading videos and other resources from KCL's Keats e-learning platform. 

By default, it remembers the content you've already downloaded, so will skip it subsequently when you need to get the more recent files. Works on most module pages but there are some edge cases where it might run into issues.


### Requirements
 - Python 3
 - Works on Linux, Windows WSL, macOS

### Installation
1. Clone this repository: `git clone https://github.com/mannmann2/keats_crawler.git`
1. `cd keats_crawler`
1. `pip install -r requirements.txt`
1. [Download chromedriver](https://chromedriver.chromium.org/downloads) for your version of Chrome
1. `sudo apt install ffmpeg`

### Usage
1. Self enrol in the Keats module, if not already enrolled
1. Update `config.py` (See below. Cookies must be updated each time your session expires)
1. Run: `python crawl.py`

### Usage for downloading videos from Microsoft Streams
1. Get video links and access token from https://web.microsoftstreams.com
1. Run: `python msstram.py`

### Config settings
`MODULE`: Name of module and the folder in which to download files  
`URLS`: Mapping between Module names and their Keats urls  
`PATH`: Location in which to create the module folder  
`PATH_TO_CHROMEDRIVER`: Location of chromedriver executable  
`COOKIES`: Copy and add cookies from your browser after logging into Keats. These can be found by navigating to the Network tab of the browser inspector.  
`DOWNLOAD_RESOURCES`: True/False - Download the non-video resources (ppt, pdf, py, etc)  
`DOWNLOAD_VIDEOS`: True/False - Download videos embedded in Keats (Won't work for videos linked on some other website)  
<!-- `DOWNLOAD_FOLDERS`: True/False - Download resource folders -->
`VIDEO_PROMPT`: True/False - Prompt before extracting each video for download (Disabling this will automatically download all extracted videos)  
`VIDEO_LIMIT`: Integer or None - Limit the number of videos extracted  
`SKIP_DUPLICATES`: True/False - To skip files already downloaded (Only works if the previous downloads occurred using this package)  
`REMEMBER_DOWNLOADS`: True/False - Add files being downloaded in current crawl to a duplicate filter (Used to check duplicates)  

`MS_STREAMS_LINKS`:  Links to videos on Microsoft Stream
`MS_STREAMS_ACCESS_TOKEN`: Authorization token to Microsoft Stream internal API
``:

* Free software: MIT license
