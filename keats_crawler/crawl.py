"""Main module."""
from config import *

import os
import re
from threading import Thread

import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup
from m3u8downloader.main import M3u8Downloader

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


def remember(url, anchor):
    code = url.split('=')[-1]
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
    driver.switch_to.default_content()
    return name, m3u8


def vid_download(name, m3u8):
        name_ = re.sub(r'[\\/:*?"<>|]', '.', name)
        path = f'{PATH}{name_}.mp4'

        M3u8Downloader(m3u8, path).start()

        print(f'--- {name} ... Done')


def run():

    print('Starting...')

    driver.get('https://keats.kcl.ac.uk/my')

    for k, v in COOKIE_DICT.items():
        driver.add_cookie({'name': k, 'value': v})

    driver.get(URLS[MODULE])

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
        for i, (anchor, url) in enumerate(res_links):
            th = Thread(target=res_download, args=(url, anchor))
            th.start()
            threads.append(th)

        for th in threads:
            th.join()

        print('Done')


    if DOWNLOAD_VIDEOS:
        if VIDEO_LIMIT:
            vid_links = vid_links[:VIDEO_LIMIT]

        print('Found', len(vid_links), 'videos')
        print('Extracting video links...')

        ch = 'y'
        for i, (anchor, url) in enumerate(vid_links):

            if VIDEO_PROMPT:
                ch = input(f'Download {anchor}? (y/n) ')

            if ch in ['y', 'Y']:
                driver.get(url)
                iframe = driver.find_element_by_xpath("//iframe[@class='mwEmbedKalturaIframe'] | //iframe[@id='contentframe']")
                name, m3u8 = parse_frame(iframe)
                VIDEO_DICT[name] = (m3u8, url, anchor)

        # threads = []
        for name, (m3u8, url, anchor) in VIDEO_DICT.items():

            vid_download(name, m3u8)

            if REMEMBER_DOWNLOADS:
                remember(url, anchor)

        #     th = Thread(target=vid_download, args=(name, m3u8))
        #     th.start()
        #     threads.append(th)

        # for th in threads:
        #     th.join()

        print('Done')
    driver.quit()

if __name__ == '__main__':
    run()
