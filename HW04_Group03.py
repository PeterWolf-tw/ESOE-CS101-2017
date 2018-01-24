#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#上繳作業前，請另存一份 "HW05_GroupXX.py"，那個 xx 就是你們的組別編號。 (如果不知道自己組別的，可從 CEIBA 上查詢。)
#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。

crewDICT = {1: {"姓名": "李鼎翊",
                "學號": "B06505029"},
            2: {"姓名":"謝心默",
                "學號":"B06505017"},
            3: {"姓名":"沈揚",
                "學號":"B06505018"},
            4: {"姓名":"韋昊臣",
                "學號":"B06505031"}
            }
#可利用程式進入點讓程式的結構更完整。

# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct

sound = wave.open("44100.wav")
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()

showAll = False # Show all data in raw string at once.
if showAll == True:
    tapeAll = sound.readframes(nframes)
    #print (tapeAll)
else:
    resamp = []
    for i in range(0, nframes):
        waveData = sound.readframes(1)
        tapeClip = struct.unpack("<h", waveData)
        #print(tapeClip)
        resamp.append(tapeClip[0])

sound.close()

sound_1 = wave.open("11025.wav", "w")
sound_1.setparams((1, 2, 11025, 110250, 'NONE', 'not compressed'))

for i in range(0,nframes,4):
    packed_value = struct.pack('h', resamp[i])
    sound_1.writeframes(packed_value)

sound_1.close()


# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"

print (b1.decode("cp950"))
print (b2.decode("UTF-8"))
print (b3.decode("UTF-16"))

# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
s_cp950 = s0.encode("cp950")
s_utf8 = s0.encode("UTF-8")
s_utf16 = s0.encode("UTF-16")

print (s_cp950)
print (s_utf8)
print (s_utf16)

# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a). 哪一種傳輸方式較為耗電？

print("Wifi")

# (b). 哪一種傳輸方式較快速？

print("Wifi")

# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。

print("手機Bluetooth規格：htc desire 816 Bluetooth 4.0")
print("傳輸速度理論值24Mbps, 照片大小941.22KB, 傳輸時間理論值=(941.22*8)/24000=0.31374秒")
print("實際耗時:約十一秒")
print("影響因素:訊號的干擾、收發端距離、手機解讀需時間")
