#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR =Turing machine是一種抽象數學計算模型。它的目的在於模仿人腦的邏輯演算程序，進而解決問題。它的構成分成三大部分:1.無限長的紙帶
                    2.一個讀寫頭 3.一套規則。紙帶可以想成是解決問題的平台，它被畫為一格格的格子，而每個格子有起始符號。當演算終了時，紙袋上的值就
                    是答案。而讀寫頭則是扮演輸入/輸出的腳色。讀寫頭會讀取它所在的格子上之符號，並將其傳送至規則，根據規則的敘述，它會改寫格子內的
                    值，並移到下一個特定的格子。不斷重複直到規則回傳終止。規則是整套演算法的邏輯依據。規則必須要詳述在每一種狀況，讀寫頭讀進任一值
                    ，讀寫頭要如何改寫並且移動到哪一格，並且必須包括結束的條件。根據不同的問題，我們可以設計不同的規則來解決。
    vonNewmannModelSTR = '''
    
    '''
    
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
