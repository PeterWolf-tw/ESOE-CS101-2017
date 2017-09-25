#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''
        Turing Model是一種模擬計算的模型。它主要是由三個部分所組成，一條無限左右延伸的紙帶(有編號)用以記錄狀態(0或1)、一個能夠左右移動的讀寫頭用以輸入輸出還有一個紀錄邏輯規則的表。當圖靈機開始運作時，讀寫頭會讀取紙帶的當前狀態，在由表決定該寫入紙帶的值(0或1)還有決定讀寫頭的移動(左、右或不動)，重複動作直到停止。
    '''
    
    vonNewmannModelSTR = '''
        vonNeUmannModel是一種電腦的模型。它是由四的部分所組成，memory, arithmetic logic unit(ALU), control unit, input/output。其中的創新就是memroy的部分結合了universal turing machine裡的紙帶(data)還有表(program)，而ALU用以邏輯計算處理資料，control unit則是控制其他三個部分，最後input/output就是負責輸入輸出。
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
