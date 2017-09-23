#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''是一個理想中的機器構想，主要有四部分。有一條想像的無限長紙帶(Tape)，與一個能讀寫紙條上資訊的讀寫頭(Head)，附有一套
    控制規則(Table)，控制讀寫頭在接收到紙條上的資訊後的動作，還有一個暫存器能記錄機器的目前狀態。紙條上有分段區域，分別存有不同資訊，而當讀寫
    頭讀到不同資訊時會依控制規則的指示執行相對應的工作，而暫存器則能記錄這些狀態，供使用者操作。
    '''
    
    vonNewmannModelSTR = '''共有五大部分。有記憶體(Memory Unit)，可用來儲存程式與資料；有算術邏輯單元(ALU)，可用來執行資訊的運算；有控制單元
    (Control Unit)確保其他部分的順利進行與一些控制；輸入與輸出部分(I/O)，接收與發送處理前與處理後的資訊，各部分可互相溝通分享資料
    
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
