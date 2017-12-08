#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#上繳作業前，請另存一份 "HW05_GroupXX.py"，那個 xx 就是你們的組別編號。 (如果不知道自己組別的，可從 CEIBA 上查詢。)
#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "莊凱崴",
                "學號": "B05107004"},
            2: {"姓名":"",
                "學號":""},
            3: {"姓名":"",
                "學號":""},
            }


# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct
import os
import sys
import audioop
sound = wave.open(os.path.split(os.path.realpath(__file__))[0]+ r"\44100.wav")
soundNew = wave.open(os.path.split(os.path.realpath(__file__))[0]+ r"\44100.wav")

#sound = wave.open(os.getcwd()+".\44100.wav")VS會把這個檔案丟去programfiles的python資料夾執行，這樣寫會找不到
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()

showAll = True # Show all data in raw string at once.
if showAll == True:
    tapeAll = sound.readframes(nframes)
    
else:
    for i in range(0, nframes):
        waveData = sound.readframes(1)
        tapeClip = struct.unpack("<h", waveData)
        print(tapeClip)
f = open(os.path.split(os.path.realpath(__file__))[0]+ r"\11025.wav", 'wb')
newWave = wave.open(f,'wb')
n_frames = soundNew.getnframes()
data = soundNew.readframes(n_frames)
#print(data)
converted = audioop.ratecv(data, 2, 1, 44100, 11025, None)
#print(converted[0])
#print(converted[1])
cc=str(converted[0])
newWave.setparams((1, 2, 11025, 0, 'NONE', 'Uncompressed'))


newWave.writeframes(converted[0])

soundNew.close()
newWave.close()

# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b'\xa5x\xa4j\xa4u\xac\xec'
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"

print(b1.decode('big5','strict'))
print(b2.decode('UTF-8','strict'))
print(b3.decode('utf-16','ignore'))

# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
s_cp950 = b""
s_utf8 = b""
s_utf16 = b""
print(s0.encode("cp950","strict"))
print(s0.encode("utf-8","strict"))
print(s0.encode("utf-16","strict"))

# 第四題：請說明 Wifi 和 Bluetooth 之間...

# (a). 哪一種傳輸方式較為耗電？

print("Wifi")
# (b). 哪一種傳輸方式較快速？

print("不一定，看版本，802.11ac > BT 5.0 > 802.11b")

# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。

print("Sony Z5 Premium最高支援BT4.0(24Mbps)，一張57.03KB的照片用藍牙4.0傳輸，理論上需57.03*8/24000=0.01901秒")
print("實際耗時約5秒")
print("系統編碼需時、傳輸時受到干擾(旁邊有2.4G的WIFI)、系統解碼需時等等")
