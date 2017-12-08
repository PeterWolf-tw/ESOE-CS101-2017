#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''一台為了模仿人的運算過程的假想機器，首先分成4個部分，第一個是無限長的紙帶(tape)
    分成無限多個格子，其中每個格子上都有一個符號，第二個則是讀寫頭(head)，它能讀出當前所在格子中的符號並對此
    當前符號做出改變，第三個是一套運算規則(table)，這規則能告訴讀寫頭該做什麼事以及接下來要做的事，最後一個則
    是狀態儲存器，負責儲存目前的狀態，狀態儲存器只能保存有限個狀態。在運算過程中首先把符號串由左填至紙帶的格子
    中，依照狀態機中的狀態，讀寫頭去讀當前的符號並依照運算規則決定下一步該如何，運算完之後更新狀態機的狀態，並
    持續接下來的步驟。
    
    '''
    
    vonNewmannModelSTR = '''一台能儲存程式與資料的機器，因為運算規則與資料都要儲存在記憶體中，因此兩者的格式
    要一樣，之前的Turing Model因為只擁有一個運算規則，因此只能做一項工作，但von Newmann Model可以在記憶體中
    改變它的運算規則，也讓這台機器可以做更多工作。這台機器分成了五個部分(1)記憶體(2)算術邏輯單元(3)控制單元
    (4)輸入(5)輸出，當在運算時，它會去記憶體中尋找特定資料以及特定運算規則並送往CPU(算術邏輯單元以及控制單元)
    ，當CPU算完後再將結果儲存在記憶體中'''
    
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
