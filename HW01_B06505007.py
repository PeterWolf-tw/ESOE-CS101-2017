#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = ''' Turing Model是一台假想機器，能模仿人的運算過程。它有一條無限長的紙帶、一個讀寫頭、
    一套運算規則和一個狀態暫存器。紙帶被劃分為無限多個格子，用來紀錄符號，讀寫頭則能讀出符號，並且依據運算規則
    改變符號，暫存器用來儲存當前的狀態。而整個機器會運算到沒有適用的指令為止。'''
    
    vonNewmannModelSTR = '''vonNewmann Model將運算規則也儲存在記憶體中，且與資料以相同的格式被儲存，透過改
    變規則來完成各種運算，也可以視為許多個Turing machine的結合。'''
    
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
