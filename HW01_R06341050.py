#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''圖靈機為一種由Alan Turing提出的抽象模型。
由一條無限長的紙帶、一個可左右移動的讀寫頭、一個存儲（state)狀態的暫存器盒子以及能對盒子下指令的成事所組成。
透過製造簡單但運算能力極強的機械裝置，根據每一時刻讀寫頭所讀到的資訊和當時內部狀態進行核對，來確定它下一時刻的內部狀態和輸出動作。'''

    
    vonNewmannModelSTR = '''現今電腦計算機的通用架構。
將電腦分成五大原件，分別為儲存器（記憶體）、運算器、控制器以及輸出/輸入器。
在這馮紐曼模型的概念中，只要將程式透過輸入器載入記憶體中，運算過後再透過控制器告訴電腦要用哪個輸出器執行。 '''
    
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
