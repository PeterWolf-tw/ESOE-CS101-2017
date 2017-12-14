#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#上繳作業前，請另存一份 "HW05_GroupXX.py"，那個 xx 就是你們的組別編號。 (如果不知道自己組別的，可從 CEIBA 上查詢。)
#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "陳奕舟",
                "學號": "b06505006"},
            2: {"姓名": "袁肇謙",
                "學號": "b06505022"},
            3: {"姓名": "蔡育勝",
                "學號": "b06505024"},
            4: {"姓名": "王曦",
                "學號": "b06505040"},            
            }

# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct

sound = wave.open("./44100.wav")
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()
values = []

showAll = False # Show all data in raw string at once.

if showAll == True:
    tapeAll = sound.readframes(nframes)
else:
    for i in range(0, nframes):
        waveData = sound.readframes(1)
        tapeClip = struct.unpack("<h", waveData)
        samp.append(tapeClip[0])
        print(tapeClip)


new = wave.open("777.wav",'w')
new.setparams((1, 2, 11025, 110250, 'NONE', 'not compressed'))


for i in range(0,nframes,4):
    packed_value = struct.pack('h', samp[i])
    new.writeframes(packed_value)
    
new.close()


# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"

print(b1.decode('cp950','strict'))
print(b2.decode('utf-8','strict'))
print(b3.decode('utf-16','strict'))

# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
s_cp950 = b"\xadp\xba\xe2\xbe\xf7\xb7\xa7\xbd\xd7\xbbP\xb5{\xa6\xa1\xb3]\xadp"
s_utf8 = b"\xe8\xa8\x88\xe7\xae\x97\xe6\xa9\x9f\xe6\xa6\x82\xe8\xab\x96\xe8\x88\x87\xe7\xa8\x8b\xe5\xbc\x8f\xe8\xa8\xad\xe8\xa8\x88"
s_utf16 = b"\xff\xfe\x08\x8a\x97{_j\x82i\xd6\x8a\x07\x82\x0bz\x0f_-\x8a\x08\x8a"

print(s0.encode("cp950"))
print(s0.encode("UTF-8"))
print(s0.encode("UTF-16"))


# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a). 哪一種傳輸方式較為耗電？
# Answer:藍芽的功率需求比WiFi低，因此裝置體積也較小，適用於消費電子產品。
# (b). 哪一種傳輸方式較快速？
# Answer:藍芽傳輸速度720kbps(千位元/秒)，Wi-Fi則為11mbps(百萬位元/秒)，速度上有明顯差距。
# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。
# A(c).htc desire 828 Bluetooth 4.2
#      htc U11 Bluetooth 5.0
#      Bluetooth 4.2 傳輸速度理論值25Mbs，照片大小2.42MB，傳輸時間理論值(2.42*8/25=0.88s)
#      實際傳輸時間約19秒
#      影響因素:附近的其他wifi、3G/4G、電源、金屬等干擾