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


# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct

sound = wave.open("./44100.wav")
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()

showAll = True # Show all data in raw string at once.
if showAll == True:
    tapeAll = sound.readframes(nframes)
else:
    for i in range(0, nframes):
        waveData = sound.readframes(1)
        tapeClip = struct.unpack("<h", waveData)
        print(tapeClip)

filepath='./44100.wav'
outputfile = filepath+'output.wav'
outputData = tapeAll
outputwave = wave.open(outputfile, 'wb')
framerate = int(11025)
outputwave.setparams((nchannels, sampwidth, framerate, nframes,comptype, compname))
outputwave.writeframes(outputData)
# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"

# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
s_cp950 = b"\xadp\xba\xe2\xbe\xf7\xb7\xa7\xbd\xd7\xbbP\xb5{\xa6\xa1\xb3]\xadp"
s_utf8 = b"\xe8\xa8\x88\xe7\xae\x97\xe6\xa9\x9f\xe6\xa6\x82\xe8\xab\x96\xe8\x88\x87\xe7\xa8\x8b\xe5\xbc\x8f\xe8\xa8\xad\xe8\xa8\x88"
s_utf16 = b"\xff\xfe\x08\x8a\x97{_j\x82i\xd6\x8a\x07\x82\x0bz\x0f_-\x8a\x08\x8a"
print(s0.encode('cp950'))
print(s0.encode('utf-8'))
print(s0.encode('utf-16'))


# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a). 哪一種傳輸方式較為耗電？
print("藍牙。因為其功率較低，所以比較省電")
# (b). 哪一種傳輸方式較快速？
print("wifi")
# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。

#以下的 print() 無法執行。

print( 手機型號: samsung SM-G950FD
      藍牙規格:  bluetooth 5.0
      傳送照片大小:19.4MB
      傳送照片解析度:1080x1402
      理論傳輸時間 = 0.647 sec
      實際傳輸時間 = 10'19
      影響傳送時間的因素:
        1.發射功率
        2.接收靈敏度
        3.外界對訊號的干擾
        4.訊號傳輸中的耗損
        5.編碼的格式
        6.封包大小''')
