#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''    Turing Model 是一種被設計來模擬人類進行學數學運算的機器，
    相較於一般的Computer，圖靈機多了Program的元素，這讓它可以更靈活地使用Input data和
    Program做出更複雜的判斷和行為。Turing Model包含了幾樣元素:一條無限長的紙帶，上面
    的    每一小格都給予了各種符號；Program，視為運算的操縱端；讀寫頭，用以讀取紙帶上
    的符號；狀態，Program運行的依據。運算的一開始讀取頭會在紙帶初始位置讀取一個符號，
    Program根據收到的數據及初始位置的狀態進行使讀取頭向左或向右的判斷，而在狀態被更改
    為終止狀態之前，Turing Model則會不斷運作。

    '''

    vonNewmannModelSTR = '''von Newmann Model 是一種在Turing Model的基礎架構下，將
    程式內部化於電腦的新型概念，在von Newmann Model的結構中，Program以Data的形式存在
    於記憶體中，這使得電腦內部的運作更趨向於分工化，執行也更有效率，也藉由將程式寫入，
    電腦中，節省了許多時間，總而言之von Newmann Model可以說是電子計算機演進中的一大進
    步。

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