#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''Turing Model 是利用機器模仿人類運算數學的過程，包含一條無限長的紙帶、一個讀寫頭、一套控制規則及一個狀態暫存器。
    在讀寫頭讀取紙帶上的訊息(input)後，依目前狀態暫存器內的控制規則控制讀寫頭改變紙帶上的記號(output)，並控制讀寫頭往左或右移動，直到遇到控制規則中的停止訊號。

'''

    vonNewmannModelSTR = '''von Neumann Model分為四個部分:記憶體(memory)、算術邏輯單元(arithmetic logic unit)、控制單元(control unit)及輸入與輸出(input/output)。
    與早期電腦最大的不同是除了資料(data)以外，程式(program)也儲存在記憶體內，並且同樣以二進位的方式儲存。
    運作方式則是在控制單元讀取記憶體中程式的指令後解碼並"依照順序"執行。

    '''
    #通常我們會避免寫出左右太「寬」的程式碼。
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
