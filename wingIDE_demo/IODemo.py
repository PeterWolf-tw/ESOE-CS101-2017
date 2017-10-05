#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def main():
    inputFILE = open("./news.txt", encoding="utf-8").read()

    #for 迴圈：計算整篇文字從頭到尾有幾個逗號
    counter = 0
    for i in range(0, len(inputFILE)):
        if inputFILE[i] == "，":
            counter = counter + 1
        else:
            pass
    print("逗號有：", counter, "個")

    #while 迴圈：不知道什麼時候遇到結尾，總之先找出第一個冒號前的字元。
    flag = ""
    index = 0
    while flag != "：":
        flag = inputFILE[index]
        index = index + 1
    print(inputFILE[index-4:index])

if __name__== "__main__":
    main()