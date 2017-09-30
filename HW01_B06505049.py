#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''由紙帶,讀寫頭,狀態暫存器及控制規則所組成的機器,模仿人類的數學計算,其中紙帶上記錄著資訊,
    由讀取頭讀取,並根據控制規則進行下一步動作,由狀態暫存器紀錄當前的狀態
    
    '''
    
    vonNewmannModelSTR = '''一種將程式指令記憶體和數據記憶體合併在一起的電腦設計概念架構,將電腦分為記憶體,運算邏輯單元,控制單元和I/O,
    由於記憶體同時處理數據和指令,因此二者必須以相同格式表達
    
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
