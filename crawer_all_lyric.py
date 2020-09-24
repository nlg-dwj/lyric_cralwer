# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq
import jsonpath
import pandas as pd
import time
import random
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}


def restaurant(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except Exception:
        print('此页有问题！')
        return None


def get_json(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json_text = response.json()
            return json_text
    except Exception:
        print('此页有问题！')
        return None


def get_playlist(url):
    data2 = []
    doc = get_json(url)
    jobs = doc['result']['tracks']
    for job in jobs:
        dic = {}
        dic['name'] = jsonpath.jsonpath(job, '$..name')[0]  # 歌曲名称
        dic['id'] = jsonpath.jsonpath(job, '$..id')[0]  # 歌曲ID
        data2.append(dic)
    return data2


def get_list():
    list1 = []
    for i in range(0, 35, 35):  # 跑一页试试，如果跑全部，改为 range(0,1295,35)
        url = 'https://music.163.com/discover/playlist/?order=hot&cat=%E5%8D%8E%E8%AF%AD&limit=35&offset=' + str(i)
        print('已成功采集%i页歌单\n' % (i / 35 + 1))
        data2 = []
        html = restaurant(url)
        doc = pq(html)
        for i in range(1, 36):  # 一页35个歌单
            a = doc('#m-pl-container > li:nth-child(' + str(i) + ') > div > a').attr('href')
            a1 = 'https://music.163.com/api' + a.replace('?', '/detail?')
            data2.append(a1)
        list1.extend(data2)
        time.sleep(5 + random.random())
    return list1


playlist_url = get_list()
data2 = pd.DataFrame(columns=('name', 'id'))  # 建个空

for i in playlist_url[0:]:
    print(i)
    playlist = get_playlist(i)
    a = pd.DataFrame(playlist)

    time.sleep(5 + random.random())
    data2 = pd.concat([data2, a])
    data3 = data2.drop_duplicates(subset=None, keep='first', inplace=False)  # 去重
    data3.to_csv("huayu_data.csv", index_label="index_label", encoding='utf-8-sig')  # 此表一会儿用到