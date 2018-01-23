#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''
    Turing Model，含有1.紙帶，紀錄所要運算的數字，2.讀寫頭，讀取現在的數字，3.狀態機(運算方法)，裡面描述了各狀態之間的關係，4.暫存狀態，紀錄現在狀態以得知接下來該如何改變，利用讀取改寫紙帶上的內容、狀態之間的改變，模擬人所做的運算。
    '''

    vonNewmannModelSTR = '''
    von Newmann Model，將Turing Model的運算方法轉換為一組資料，利用輸入不同運算方法，來達到做不同運算的目的。
    '''

    if model == "Alen Turing":
        print(turingModelSTR)
    elif model == "von Newmann":
        print(vonNewmannModelSTR)
    else:
        pass

    #三個單引號或雙引號就可以換行了。
    #通常我們會避免寫出左右太「寬」的程式碼。
if __name__ == "__main__":
    modelPrinter("Alen Turing")
    print("=====我是分隔線=====")
    modelPrinter("von Newmann")
