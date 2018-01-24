#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#上繳作業前，請另存一份 "HW05_GroupXX.py"，那個 xx 就是你們的組別編號。 (如果不知道自己組別的，可從 CEIBA 上查詢。)
#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "莊博翰",
                "學號": "B06505004"},
            2: {"姓名":"張在然",
                "學號":"B06505002"},
            3: {"姓名":"凃皓瑋",
                "學號":"B06505001"},
            4:{"姓名":"林鴻儒",
                "學號":"B04207001"}
            }


# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct

sound = wave.open("./44100.wav")
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()
print(sound)

showAll = True # Show all data in raw string at once.
if showAll == True:
    tapeAll = sound.readframes(nframes)
else:
    for i in range(0, nframes):
        waveData = sound.readframes(1)
        tapeClip = struct.unpack("<h", waveData)
        print(tapeClip)

filepath='./44100.wav'


outData = tapeAll
outfile = filepath+'new.wav'
outwave = wave.open(outfile, 'wb')



framerate = int(11025)

outwave.setparams((nchannels, sampwidth, framerate, nframes,
    comptype, compname))
outwave.writeframes(outData)

#你的 outwave 沒有產生任何檔案。少了一步。




# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"

B1=b1.decode('cp950','strict')
B2=b2.decode('UTF-8','strict')
B3=b3.decode('UTF-16',"strict")
print(B1,'\n',B2,'\n',B3,'\n')
# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"

s_cp950 = s0.encode('cp950','strict')
s_utf8 = s0.encode('UTF-8','strict')
s_utf16 = s0.encode('UTF-16','strict')
print(s_cp950,'\n',s_utf8,'\n',s_utf16,'\n')


# 第四題：請說明 Wifi 和 Bluetooth 之間...
print(''' (a). 哪一種傳輸方式較為耗電？
     藍牙功率較低，所以較省電
 (b). 哪一種傳輸方式較快速？
      WIFI傳輸速度較快
 (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
      傳送？ 最後並請列出所有可能影響傳送時間的因素。
      手機型號: htc desire 626 , samsung SM-G950FD
      藍牙規格: bluetooth 4.1  , bluetooth 5.0
      傳送照片大小:19.4MB
      傳送照片解析度:1080x1402
      bluetooth 4.0理論最高傳輸速度(3MB/s)
      理論傳輸時間 = 1.94 / 3 = 0.647 sec
      實際傳輸時間 = 10秒19
      影響傳送時間的因素:
        1.發射功率
        2.接收靈敏度
        3.外界對訊號的干擾
        4.訊號傳輸中的耗損
        5.編碼的格式
        6.封包大小''')

