#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''turingModel 是 Alan Turing 提出的一個想法，他將人類的計算過程藉由兩個機械化的動作來表現，1：更改當前位置中的符號 2：從當前位置往作或右邊移動
                        而為了要達成這兩個步驟，他假想出一部機器即turingmachine，在這個機器當中，他有一條無限長的紙帶，紙帶被切割成很多格子，每個格子裡面只能
                        寫下一個符號，然後他有一個讀寫頭，這個讀寫頭只會停留在紙帶上的一個格子上，他可以讀入和改變當前格子中的符號，並可以任意向左右移動，還需要有
                        一套program用來控制讀寫頭的動作，program必須包含initial state和halting state。
    
    '''
    
    vonNewmannModelSTR = '''vonneumannModel 是將電腦分成4個子系統，分別是memory，arithmetic logic unit，control unit，input/output，然後將電腦的
                            program和data都寫入memory，因此program在vonneumannModel下就可以被更改，因此概念上更接近universal turing machine
    
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
