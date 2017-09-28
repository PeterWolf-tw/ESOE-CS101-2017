#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = ''' A turing machine is a mathematical model of computation invented by 
    Alan Turing. It operates on an infinite memory tape that contains discrete message, or cells, 
    also, it read/write the messege through a "head". After reading a messege from the tape, the 
    machine translate this massege from the "table", output the result based on the current state 
    of machine. The output contains the logic how to modify the current state and the messege on 
    the tape.
    '''
    
    vonNewmannModelSTR = ''' The major differences between Turing model and von Neumann model is 
    that the "table" used to translate messege is an additional input, that is, the logic of how 
    to translate the input is "user-friendly".
    von Neumann model是一種將程式指令記憶體和資料記憶體合併在一起的電腦設計概念架構。可分為四個子系統：記憶體、算術邏輯單元、控制單元、
    輸入/輸出。記憶體：顧名思義是一個儲存資料及程式的區域。算術邏輯單元：是執行算數及邏輯計算的地方。控制單元：用來控制記憶體、算術邏輯
    單元及輸入/輸出子系統的運作。輸入/輸出：輸入子系統接受資料及來自電腦外部的程式，而輸出子系統則是將運算處理的結果傳送至電腦外部。
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
