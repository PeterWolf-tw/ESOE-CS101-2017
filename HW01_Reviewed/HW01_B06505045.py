#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。

#助教：你繳上來的作業程式無法執行啊！

def modelPrinter(model):
    turingModelSTR = '''Turing machine是一種模仿人腦的邏輯演算程序的抽象數學計算模型。它由三部分所構成:1.無限長的紙帶(tape)2.一個讀寫頭(head) 3.一套運算規則(table)。紙帶上有一格格的格子，而每個格子有起始符號。當演算終了時，紙帶上的值就
                    是答案。而讀寫頭則是扮演input/output的角色。讀寫頭會讀取它所在的格子上的符號，然後依規則傳送，根據規則它會改寫格子內的值，移到下一個特定的格子直到規則回傳終止。運算規則是整套演算法的邏輯依據。規則詳述在每一種狀況，讀寫頭讀進任一值
                    ，讀寫頭要如何改寫並且移動到哪一格且必須包括結束的條件。根據不同的問題，我們可以設計不同的運算規則來解決。
    
    '''
    
    vonNewmannModelSTR = '''Von Neumann model 是Universal Turing Machine的一種應用。它的構成分成5個部分:1.input 2.memory 3.control unit 4.arithmetic logic unit 5.output。input可以是data或program。輸入後會被儲存到memory中。而control unit會到memory中讀取其中的program後解碼且讀取指令，執行完畢
                         後再將結果回傳到memory 儲存，並且輸出至output。Arithmetic logic unit 是算術邏輯元件，負責在ontrol unit執行程式時進行邏輯判斷或者算術運算'''
    
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
