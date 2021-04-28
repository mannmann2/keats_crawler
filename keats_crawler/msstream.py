import os
import requests
import subprocess
from threading import Thread

from config import MS_STREAM_ACCESS_TOKEN, MS_STREAM_LINKS
from config import PATH, MODULE

LINKS = []
PATH = f'{PATH}{MODULE}/'
if not os.path.exists(PATH):
    print('Creating directory at', PATH)
    os.makedirs(PATH)


def download_stream(m3u8, path):
    cmd = f'ffmpeg -headers -i {m3u8} -c copy -bsf:a aac_adtstoasc -threads 8'.split()
    cmd.insert(2, f'Authorization: {MS_STREAM_ACCESS_TOKEN}')
    cmd.append(path)
    subprocess.run(cmd)


for link in MS_STREAM_LINKS:

    name = f'Lecture {name}'
    vid_id = link.split('/')[-1]

    with requests.Session() as s:
        headers = {'Authorization': MS_STREAM_ACCESS_TOKEN}
        s.headers.update(headers)
        # $expand=creator,tokens,status,liveEvent,extensions&
        details = s.get(f'https://euno-1.api.microsoftstream.com/api/videos/{vid_id}?api-version=1.4-private').json()
        path = PATH + details['name'] + '.mp4'
        m3u8 = details['playbackUrls'][-1]['playbackUrl']
        print(path, m3u8)
        LINKS.append((m3u8, path))

threads = []
for i, (m3u8, path) in enumerate(LINKS):
    th = Thread(target=download_stream, args=(m3u8, path))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

print('Done')
