# Quick Links...

# MODULE = 'Machine Learning'
MODULE = 'Data Mining'
# MODULE = 'Pattern Recognition'
# MODULE = 'Distributed Ledgers'
# MODULE = 'Nature Inspired Learning Algorithms'

URLS = {
    'Machine Learning': 'https://keats.kcl.ac.uk/course/view.php?id=89936',
    'Data Mining': 'https://keats.kcl.ac.uk/course/view.php?id=77818&section=10',
    'Pattern Recognition': 'https://keats.kcl.ac.uk/course/view.php?id=77831',
    'Distributed Ledgers': 'https://keats.kcl.ac.uk/course/view.php?id=77817',
    'Nature Inspired Learning Algorithms': 'https://keats.kcl.ac.uk/course/view.php?id=86406'
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

# Run in headless mode. Let it be true unless you know a bit about selenium
HEADLESS = True


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
