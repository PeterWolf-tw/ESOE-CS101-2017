#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01
#just for test

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''有一個很長的紙帶，有很多格子上面寫著0或1
                        現在有個我們要解決的問題，被記錄成初始狀態。然後我們要解決的方法被寫成一個程式。這個程式會引導讀寫頭的行為
                        讀寫頭可以看現在是0or1然後根據程式的指示
                        往左或往右或不動。改變數字與否。跳到哪個狀態。
                        最後，當讀寫頭讀到halt時候，這項問題就被解決了並且最後紙帶上的樣子就是答案。'''    
    vonNewmannModelSTR = '''其實就是在一個機器儲存很多程式然後根據不同的目標，來使用想用的程式。剩下的運作，就是依照上述的圖靈機了吧'''
    
    if model == "Alen Turing":
        print(turingModelSTR)
    elif model == "von Newmann":
        print(vonNewmannModelSTR)
    else:
        pass
        
        
if __name__ == "__main__":
    modelPrinter("Alen Turing")
    print("=====我是分隔線=====")
    modelPrinter("von Newmann")
