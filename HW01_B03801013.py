#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''由紙帶、讀寫頭、控制規則、狀態暫存器幾個部分所組成的機器，其中紙帶記錄資訊，由讀寫頭讀取當下狀態，並根據控制規則改變當下狀態，並用狀態暫存器純存當下狀態，以此模擬人類來運算。
    
    '''
    
    vonNewmannModelSTR = '''將電腦分成memory、arithmetic logic unit、control unit、input/output四個部分，再將電腦的program和data都寫入memory，因此program在vonneumannModel下就可以被更改，是一種universal turing machine。
    
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
