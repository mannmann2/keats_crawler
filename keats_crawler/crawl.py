"""Main module."""
from config import *

import os
import re
import subprocess
from threading import Thread

import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

VIDEO_DICT = {}

PATH = f'{PATH}{MODULE}/'
if not os.path.exists(PATH):
    print('Creating directory at', PATH)
    os.makedirs(PATH)

options = Options()
if HEADLESS:
    options.add_argument("--headless")

driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER, options=options)


def is_duplicate(href, anchor):
    code = href.split('=')[-1]
    file = f'{code} - {MODULE}/{anchor}\n'

    with open('duplicates.txt', 'r') as f:
        files = f.readlines()

    if file in files:
        return True
    return False


def remember(href, anchor):
    code = href.split('=')[-1]
    file = f'{code} - {MODULE}/{anchor}'

    with open('duplicates.txt', 'a') as f:
        f.write(file + '\n')


def res_download(url, anchor):
    try:
        res = requests.get(url + '&redirect=1', timeout=10, cookies=COOKIE_DICT)
    except requests.exceptions.Timeout:
        print('timeout...')
        return

    name = unquote(res.url.split('/')[-1])
    name = re.sub(r'[\\/:*?"<>|]', '.', name)
    with open(f'{PATH}{name}', 'wb') as f:
        f.write(res.content)

    if REMEMBER_DOWNLOADS:
        remember(url, anchor)

    print(f'--- {name} ... Done')


def parse_frame(iframe):
    driver.switch_to.frame(iframe)
    video_frame = driver.find_element_by_xpath("//iframe[@name='kplayer_ifp']")
    driver.switch_to.frame(video_frame)

    src = driver.page_source.replace('\n', ' ')
    soup = BeautifulSoup(src, 'html.parser')
    name = soup.find('title').text

    match = re.search('\<video.*?\</video>', src)
    soup2 = BeautifulSoup(match.group(0), 'html.parser')

    m3u8 = soup2.find('video')['src'].split('?')[0]
    VIDEO_DICT[name] = m3u8
    driver.switch_to.default_content()


def vid_download(name, m3u8):
        name_ = re.sub(r'[\\/:*?"<>|]', '.', name)
        path = f'{PATH}{name_}.mp4'

        cmd = f"ffmpeg -i {m3u8} -c copy -bsf:a aac_adtstoasc".split() + [path]
        print(cmd)
        subprocess.run(cmd)

        print(f'--- {name} ... Done')


def run():

    print('Starting...')

    driver.get('https://keats.kcl.ac.uk/my')

    for k, v in COOKIE_DICT.items():
        driver.add_cookie({'name': k, 'value': v})

    driver.get(URL)


    soup = BeautifulSoup(driver.page_source.replace('\n', ' '), 'html.parser')
    links = soup.find_all('a', class_='aalink')

    if SKIP_DUPLICATES:
        vid_links = [(link.text, link['href']) for link in links if '/kalvid' in link.get('href', '') and not is_duplicate(link['href'], link.text)]
        res_links = [(link.text, link['href']) for link in links if '/resource' in link.get('href', '') and not is_duplicate(link['href'], link.text)]
    else:
        vid_links = [(link.text, link['href']) for link in links if '/kalvid' in link.get('href', '')]
        res_links = [(link.text, link['href']) for link in links if '/resource' in link.get('href', '')]


    if DOWNLOAD_RESOURCES:
        print('Downloading...', len(res_links), 'resources')

        threads = []
        for i, (anchor, link) in enumerate(res_links):

            th = Thread(target=res_download, args=(link, anchor))
            th.start()
            threads.append(th)

        for th in threads:
            th.join()

        print('Done')


    if DOWNLOAD_VIDEOS:
        print('Found', len(vid_links), 'videos')
        print('Extracting video links...')

        for i, (anchor, link) in enumerate(vid_links):

            driver.get(link)
            iframe = driver.find_element_by_xpath("//iframe[@class='mwEmbedKalturaIframe'] | //iframe[@id='contentframe']")
            parse_frame(iframe)

            if REMEMBER_DOWNLOADS:
                remember(link, anchor)

            print('.', end='')

        print('\nDownloading videos...')

        # threads = []
        for name, m3u8 in VIDEO_DICT.items():
            vid_download(name, m3u8)
        #     th = Thread(target=vid_download, args=(name, m3u8))
        #     th.start()
        #     threads.append(th)

        # for th in threads:
        #     th.join()

        print('Done')

if __name__ == '__main__':
    run()
