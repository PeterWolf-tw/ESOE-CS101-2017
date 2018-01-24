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

# 第一題
import wave
import struct

sound = wave.open('./44100.wav')
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()

box = []
for i in range(0, nframes):
    waveData = sound.readframes(1)
    tapeClip = str(struct.unpack("<h", waveData))
    x = tapeClip.index(',')
    tapeClip = int(tapeClip[1:x])
    box.append(tapeClip)

sound.close()

#可利用程式進入點讓程式的結構更完整。

G1 = wave.open('./Group01.wav', 'w')
G1.setparams((1, 2, 11025, 110250, 'NONE', 'not compressed'))

t = 0
while t in range(0, nframes):
    newsound = struct.pack('h', box[t])
    G1.writeframes(newsound)
    t = t + 4

G1.close()


# 第二題
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"
print(b1.decode('cp950','strict'))
print(b2.decode('utf-8','strict'))
print(b3.decode('utf-16','strict'))

# 第三題
s0 = "計算機概論與程式設計"
s_cp950 = b"\xadp\xba\xe2\xbe\xf7\xb7\xa7\xbd\xd7\xbbP\xb5{\xa6\xa1\xb3]\xadp"
s_utf8 = b"\xe8\xa8\x88\xe7\xae\x97\xe6\xa9\x9f\xe6\xa6\x82\xe8\xab\x96\xe8\x88\x87\xe7\xa8\x8b\xe5\xbc\x8f\xe8\xa8\xad\xe8\xa8\x88"
s_utf16 = b"\xff\xfe\x08\x8a\x97{_j\x82i\xd6\x8a\x07\x82\x0bz\x0f_-\x8a\x08\x8a"

# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a). 哪一種傳輸方式較為耗電？
print('Ans(a) = wifi')
# (b). 哪一種傳輸方式較快速？
print('Ans(b) = wifi')
# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。
print('Ans(c) = htc One M9 Bluetooth 4.1 \n'
      'htc U11 Bluetooth 5.0 \n'
      'Bluetooth 4.1 傳輸速度理論值24Mbps，照片大小2.71MB \n'
      '傳輸時間理論值0.903s (2.71*8/24=0.903s) \n'
      '實際傳輸時間約18.5秒 \n'
      '影響因素:旁邊其他的電子用品、金屬製品、電源、wifi、3G/4G等其他無線區域網路干擾、手機間的距離、考慮資料從記憶卡讀取和存取的速度')
