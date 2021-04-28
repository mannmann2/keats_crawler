import requests
import subprocess

from config import MS_STREAM_ACCESS_TOKEN, MS_STREAM_LINKS
from config import PATH, MODULE

PATH = f'{PATH}{MODULE}/'


def download_stream(url):

    vid_id = url.split('/')[-1]
    headers = {
        'Authorization': MS_STREAM_ACCESS_TOKEN,
    }

    with requests.Session() as s:
        s.headers.update(headers)
        # $expand=creator,tokens,status,liveEvent,extensions&
        details = s.get(f'https://euno-1.api.microsoftstream.com/api/videos/{vid_id}?api-version=1.4-private').json()
        path = PATH + details['name'] + '.mp4'
        m3u8 = details['playbackUrls'][-1]['playbackUrl']
        print(path, m3u8)

        cmd = f'ffmpeg -headers -i {m3u8} -c copy -bsf:a aac_adtstoasc -threads 8'.split()
        cmd.insert(2, f'Authorization: {MS_STREAM_ACCESS_TOKEN}')
        cmd.append(path)
        subprocess.run(cmd)


for video in MS_STREAM_LINKS:
    download_stream(video)
