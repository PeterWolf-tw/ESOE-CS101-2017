#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#上繳作業前，請另存一份 "HW05_GroupXX.py"，那個 xx 就是你們的組別編號。 (如果不知道自己組別的，可從 CEIBA 上查詢。)
#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。

crewDICT = {1: {"姓名": "楊欣哲",
                "學號": "B06505021"},
            2: {"姓名":"張榮顯",
                "學號":"B06505045"},
            3: {"姓名":"簡佑憲",
                "學號":"b06505050"},
            4: {"姓名":"陳祐融",
                "學號":"b06505003"},
            }



#請參考 http://chentain.pixnet.net/blog/post/44814997-python-3-%E6%8A%93%E5%8F%96%E7%BD%91%E9%A1%B5%E7%9A%84-n-%E7%A7%8D%E6%96%B9%E6%B3%95%EF%BC%9A
#並利用 urllib 和 request 兩個套件 (如果你的系統沒有，請自行安裝) 實作抓取
# http://140.112.27.24:5566/
#這個網頁中提到的三個頁面。 其中 http://140.112.27.24:5566/add?x=10&y=5 這個連結的 x 和 y 值可自定。
import urllib.request
output = urllib.request.urlopen('http://140.112.27.24:5566/')
html1 = output.read().decode('utf-8')
print(html1,'\n')

output = urllib.request.urlopen('http://140.112.27.24:5566/add?x=10&y=5')
html2 = output.read().decode('utf-8')
print(html2,'\n')

output = urllib.request.urlopen('http://140.112.27.24:5566/page')
html3 = output.read().decode('utf-8')
print(html3,'\n')
