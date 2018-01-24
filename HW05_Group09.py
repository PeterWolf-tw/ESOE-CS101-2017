#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#上繳作業前，請另存一份 "HW05_GroupXX.py"，那個 xx 就是你們的組別編號。 (如果不知道自己組別的，可從 CEIBA 上查詢。)
#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "陳心怡",
                "學號": "b06505030"},
            2: {"姓名": "楊千瑩",
                "學號": "b06505032"},
            3: {"姓名": "溫皓良",
                "學號": "b04505050"},
            }


#請參考 http://chentain.pixnet.net/blog/post/44814997-python-3-%E6%8A%93%E5%8F%96%E7%BD%91%E9%A1%B5%E7%9A%84-n-%E7%A7%8D%E6%96%B9%E6%B3%95%EF%BC%9A
#並利用 urllib 和 request 兩個套件 (如果你的系統沒有，請自行安裝) 實作抓取
# http://140.112.27.24:5566/
#這個網頁中提到的三個頁面。 其中 http://140.112.27.24:5566/add?x=10&y=5 這個連結的 x 和 y 值可自定。


import urllib.request
website = urllib.request.urlopen('http://140.112.27.24:5566/')
result = website.read()
print(result)

import urllib.request
website = urllib.request.Request('http://140.112.27.24:5566/')
data = urllib.request.urlopen(website)
result = data.read()
print(result)



import urllib.request
website = urllib.request.urlopen('http://140.112.27.24:5566/add?x=1000&y=1')
result = website.read()
print(result)

import urllib.request
website = urllib.request.Request('http://140.112.27.24:5566/add?x=1000&y=1')
data = urllib.request.urlopen(website)
result = data.read()
print(result)



import urllib.request
website = urllib.request.urlopen('http://140.112.27.24:5566/page')
result = website.read()
print(result)

import urllib.request
website = urllib.request.Request('http://140.112.27.24:5566/page')
data = urllib.request.urlopen(website)
result = data.read()
print(result)

#import 只需要做一次就行了。