#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''
    Turing model是一種用來模仿人類一些行為的機械模型。Turing提出的這個模型由三個部分組成：一條無限長的紙帶，上面由無數個區間組成，每個區間能存放兩種型態，像是打洞的有無；一個可以讀取紙帶上區間內的型態的東西，而且可以左右移動以及改變紙帶上區間的型態；一個操作的模式，功能是告訴讀取紙帶的東西說，如果現在讀到A要做什麼，讀到B時要做什麼，並且這個模式有個開始點跟結束點。Turing提出的這個模型，讓機器不只能處理一個問題，而讓建造一個多功能的機器變得可能。
    '''
    
    vonNewmannModelSTR = '''
    von Neumann Model是一個將機器的program部分儲存在memory的一個想法，這樣操作的程序不再是被固定寫死的，而是可以更改的。然而，要完成這樣的模型，program跟data就必須以相同的方式儲存在memory裡，因此如何區分program和data就變得十分重要。
    '''
    #助教：你的說明再加上同組其它成員的說明，就是最完整的答案了。
    
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
