#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:14:04 2019

@author: Kshitij Gupta <kshitijgm@gmail.com> <- i hate the nyancat dependency dude istg
"""

from bs4 import BeautifulSoup
import requests
import time

def main():
    url = 'https://android.googlesource.com/platform/manifest/+refs'
    webhookUrl = ''

    matching = []
    data = {
        "content": "AOSP 15 IS OUT <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129> <@928393531033264129>"
    }

    while len(matching) == 0:
        print('\n[*] Checking!')
        tag_list = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for li in soup.findAll('li', {'class': 'RefList-item'}):
            tag = li.findChildren('a', recursive=False)[0]['href'].split('/')[-1]
            tag_list.append(tag)
        matching = [s for s in tag_list if 'android-15' in s or 'android15' in s]
        if len(matching) > 0:
            if 'android-15-beta-2-gpl' or 'android-15-dp-2-gpl' or 'android-15-qpr1-beta-1-gpl' or 'android-15-dp-2-gpl' or 'android-15-beta-2-gpl' or 'android-15-qpr1-beta-1-gpl' in matching:
                print('wrong androd 15 :(')
                matching = []
                time.sleep(60)
            else:
                result = requests.post(webhookUrl, json = data)
                try:
                    result.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)
                else:
                    print(f"Payload delivered successfully, code {result.status_code}.")
        else:
            print('Still no Androd 15 :(')
            time.sleep(60)

if __name__ == '__main__':
    main()
