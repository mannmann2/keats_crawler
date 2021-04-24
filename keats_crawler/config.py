# Quick Links...

# MODULE = 'Machine Learning'
# MODULE = 'Data Mining'
# MODULE = 'Pattern Recognition'
# MODULE = 'Distributed Ledgers'
# MODULE = 'Nature Inspired Learning Algorithms'

URLS = {
    'Machine Learning': 'https://keats.kcl.ac.uk/course/view.php?id=89936',
    'Data Mining': 'https://keats.kcl.ac.uk/course/view.php?id=77818&section=13',
    'Pattern Recognition': 'https://keats.kcl.ac.uk/course/view.php?id=77831',
    'Distributed Ledgers': 'https://keats.kcl.ac.uk/course/view.php?id=77817',
    'Nature Inspired Learning Algorithms': 'https://keats.kcl.ac.uk/course/view.php?id=86406',
    'Agent-Based Modelling in Finance': 'https://keats.kcl.ac.uk/course/view.php?id=77803',
    'High Frequency Finance': 'https://keats.kcl.ac.uk/course/view.php?id=77824'
}


# Location in which to create the module folder
PATH = '/mnt/c/Users/arman/Desktop/Lectures/'

# Location of chromedriver executable
PATH_TO_CHROMEDRIVER = '/mnt/c/Users/arman/Desktop/notebooks/chromedriver.exe'

# Copy and add cookies from your browser after logging into Keats
COOKIES = '_ga=GA1.3.515879790.1582456300; gtm_isp_lookup=true; __zlcmid=105jQ7Y1SeNMxlN; __utma=215434893.515879790.1582456300.1613232743.1613232743.1; __utmz=215434893.1613232743.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=215434893; nmstat=7937c121-4c83-54a8-d8b9-571c314aec35; _shibsession_64656661756c7468747470733a2f2f6b656174732e6b636c2e61632e756b2f73686962626f6c657468=_dbba4e090f69f3571e15827e96ce6f4e; MoodleSession=gvp92kr52vro4cjb4t35tkjmu8'
COOKIE_DICT = dict([cookie.split('=', 1) for cookie in COOKIES.split('; ')])

# Download the non video files (ppt, pdf, py, etc)
DOWNLOAD_RESOURCES = True

# Download videos embedded in Keats
DOWNLOAD_VIDEOS = True

# Prompt before extracting each video for download
VIDEO_PROMPT = True

# Limit the number of videos extracted
VIDEO_LIMIT = None

# Skip files already downloaded
SKIP_DUPLICATES = True

# Add files being downloaded in current crawl to a duplicate filter
REMEMBER_DOWNLOADS = True

# Run in headless mode. Let it be true unless you know what is does
HEADLESS = True

# Links to videos on MS Streams
MS_STREAM_LINKS = [
    # 'https://web.microsoftstream.com/video/0ae20a10-7ba8-4610-8c0a-0f1fc9b74fca',
    # 'https://web.microsoftstream.com/video/9d196631-94d3-4c29-95ec-607e5fda9037',
    # 'https://web.microsoftstream.com/video/994e653d-0f02-4f01-a6c2-7ec46c2e6cee',
    # 'https://web.microsoftstream.com/video/5964bd67-8e1b-41d6-a972-55a33accb6ec',
    # 'https://web.microsoftstream.com/video/a81cab3f-e004-4962-90eb-216abb2dfab7',
    # 'https://web.microsoftstream.com/video/56c2c2d2-63b0-481c-94ee-46e0d5710be3',
    'https://web.microsoftstream.com/video/7b1ce6e9-898d-4fcc-b15a-5969886d9dc7',
]

# Download videos published on MS Streams (requires access token)
# DOWNLOAD_MS_STREAM = True

# Auth token for MS Stream
MS_STREAM_ACCESS_TOKEN = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiJodHRwczovLyoubWljcm9zb2Z0c3RyZWFtLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzgzNzBjZjE0LTE2ZjMtNGMxNi1iODNjLTcyNDA3MTY1NDM1Ni8iLCJpYXQiOjE2MTkyODUyNDEsIm5iZiI6MTYxOTI4NTI0MSwiZXhwIjoxNjE5Mjg5MTQxLCJhY3IiOiIxIiwiYWlvIjoiQVVRQXUvOFRBQUFBSWg2R0RiTVlHWDRuQldveU9MdWc3YXlqazh2WGs2YUZCWlhqVms2azZHTGl4a0hHVzJWbGlWb1FNbTJ6T25CczhTTmNxT2MwRGkrM0xVZFMzL2o3M0E9PSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwaWQiOiJjZjUzZmNlOC1kZWY2LTRhZWItOGQzMC1iMTU4ZTdiMWNmODMiLCJhcHBpZGFjciI6IjIiLCJmYW1pbHlfbmFtZSI6Ik1hbm4iLCJnaXZlbl9uYW1lIjoiQXJtYW4iLCJpcGFkZHIiOiIxMjAuNTkuMjkuMjIyIiwibmFtZSI6Ik1hbm4sIEFybWFuIiwib2lkIjoiZGU0MzI0NGMtYmFhOS00YzdhLWI1MTctYjgzMzJmZjk5ZjBkIiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTExMDE5ODU0ODctNDA1NTg2ODY2OC0yNTMyNjE1MzE3LTY1MzA4OCIsInB1aWQiOiIxMDAzMjAwMEZENzM2MUJEIiwicmgiOiIwLkFRVUFGTTl3Z19NV0ZreTRQSEpBY1dWRFZ1ajhVOF8yM3V0S2pUQ3hXT2V4ejRNRkFQNC4iLCJzY3AiOiJhY2Nlc3NfbWljcm9zb2Z0c3RyZWFtX3NlcnZpY2UiLCJzdWIiOiJ5UWM5Q3NscmVKNXpaQ0VtaDB4blFyS0FNWVJmSDhsd01YVjFXT0hacldNIiwidGlkIjoiODM3MGNmMTQtMTZmMy00YzE2LWI4M2MtNzI0MDcxNjU0MzU2IiwidW5pcXVlX25hbWUiOiJrMjAwMDk4OTNAa2NsLmFjLnVrIiwidXBuIjoiazIwMDA5ODkzQGtjbC5hYy51ayIsInV0aSI6InFfajhrUDZlM1UtWm4yYUhpUTVOQUEiLCJ2ZXIiOiIxLjAifQ.JYk_uS1LO0Vfs8hFrbPkQZTqab6h2HvlaAEBPR5-l4D8aw34ARC5e1W6L0MBQ3C7lkuuEhbwwPtixNeDJVNaD9KRl1c3K8_2OO2gG0ZpZCWn5ItsXPJwwvyzSweujYLjuELs1xV7ymcNKZcRo_FmDDUz2z6nQ9tl3Hw7m-Uga9JI1CLHoPuV9KWuCqowa6SGgLBFdpeqXtyY2npKs7dg6_rfupdFdhxDsF-VS9W7jxetxvrXFRQYqQp9HkHS1HzJwVFrlpgF0Vhix0Exm0Ge-BX5CiXUhNmOqsXL8VrvU_LD-w0QQxegu1i8nMpaWywvuRHE3wiXCsRRXArX6HMwRw'

# Links to other modules...

# MODULE = 'Scientific Computing for Finance'
# URL = 'https://keats.kcl.ac.uk/course/view.php?id=77834'
# MODULE = 'Cryptography'
# URL = 'https://keats.kcl.ac.uk/course/view.php?id=86407'
# MODULE = 'Fundamentals of Digital Signal Processing'
# URL = 'https://keats.kcl.ac.uk/course/view.php?id=77565'
# MODULE = 'Financial Markets'
# URL = 'https://keats.kcl.ac.uk/course/view.php?id=77653'
# MODULE = 'Dark Matter and Dark Energy'
# URL = 'https://keats.kcl.ac.uk/course/view.php?id=77729'

# MODULE = 'Computer Vision'
# URL = 'https://keats.kcl.ac.uk/course/view.php?id=86410'
# MODULE = 'Philosophy and Ethics of AI'
# URL = 'https://keats.kcl.ac.uk/course/view.php?id=77822'
# MODULE = 'Agent Based Systems'
# URL = 'https://keats.kcl.ac.uk/course/view.php?id=86405'
# MODULE = 'AI Planning'
# URL = 'https://keats.kcl.ac.uk/course/view.php?id=86602'
# MODULE = 'AI Reasoning & Decision Making'
# URL = 'https://keats.kcl.ac.uk/course/view.php?id=77775'
