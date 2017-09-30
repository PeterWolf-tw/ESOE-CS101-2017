#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''
    turing　Model是設計一種用來模擬人類思考與計算之機器的理論，此機器（圖靈機）包含輸入、讀寫頭、計算規則、狀態暫存機。輸入以字符的形式寫在
    無限長的紙帶上等待被讀寫頭讀取。讀寫頭在長紙帶左右移動，讀取到字符後會按照計算規則和讀寫頭的狀態改寫此字符，然後改變讀寫頭的狀態，接著左
    右移或不動。計算規則會告訴讀寫頭以某狀態讀到某字符時要採取什麼行動，計算規則也可以當成一種輸入。狀態暫存機用來儲存圖靈機的狀態．當圖靈機
    開始運作,以初始狀態讀取字符,改變字符和狀態之後移動，周而復始，最後到了停機狀態，紙帶上的字符就是我們要的輸出。由於圖靈機具有無限長的紙帶
    和可任意改寫的計算規則，理論上可以做出任何人類所能做的邏輯計算。
    '''
    
    vonNewmannModelSTR = '''
    von Newmann Model在概念上和turing model十分相近，但是von Newmann 進一步把機器切割成四個區塊
    :輸出／輸入、記憶體、計算邏輯單位與控制單元，並把計算規則和輸入看成相同的形式，一起納入記憶體。
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
