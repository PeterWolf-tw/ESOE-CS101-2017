#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''Turing machine 的概念是由Alan Turing 提出，目的在於用機器來模仿人類的思維，進行抽象的邏輯計算。
    Turing machine在每一運算步驟，皆有當下仿人類的思考模式，進行不同結果組合的運算；此模型分別由(1)一條無限長的紙帶Tape 
    (2)一個讀寫頭Head (3)一套控制規則Table (4)一個狀態暫存器State register　所組成。紙帶上的格子代表每個不同的狀態，讀寫
    頭則能顯示當下輸入之數值及其輸出，最後控制規則是整套系統的運算邏輯。
     
    '''
    
    vonNewmannModelSTR = '''Von newmann model亦是仿人類思維的邏輯計算機，不過相較於普通Turing machine，他是將程式指令
    記憶體與資料記憶體合併的一種運算機，也就是將program 與Input/Output視為單一系統。而此模型大致可分成(1)輸入輸出，也就是
    下的指令及結果、(2)記憶體、(3)運算系統，其中資料是以二進位編碼、(4)控制單元，則是用來控制算術邏輯。
    
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
