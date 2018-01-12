#!/usr/bin/env python3
# -*- coding:utf-8 -*-

crewDICT = {1: {"姓名": "張哲浩",
                "學號": "B06505027"},
            2: {"姓名":"謝佳峻",
                "學號":"B06505026"},
            3: {"姓名":"張力權",
                "學號":"b06505044"},
            4: {"姓名": "黃日新",
                "學號": "B06505048"}            
            }

import urllib.request
response1 = urllib.request.urlopen('http://140.112.27.24:5566/')
HTML1 = response1.read()

response2 = urllib.request.urlopen('http://140.112.27.24:5566/add?x=81000&y=19000')
HTML2 = response2.read()

response3 = urllib.request.urlopen('http://140.112.27.24:5566/page')
HTML3 = response3.read()

print(HTML2)