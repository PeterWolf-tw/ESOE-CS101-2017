Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> @ -0,0 +1,34 @@
#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''Turing model是一種模擬人類一些行為的機械模型。這個模型由三個部分組成：
一條無限長的紙帶、一個讀寫頭、一套控制規則、一個狀態紀錄器。紙帶上面由無數個區間組成，每個區間
只能存放兩種型態，像是打洞的有無；讀寫頭可以讀取紙帶上區間的型態，而且可以左右移動及改變紙帶上
區間的型態，例如將有改成無；控制規則就是操作的模式，根據目前狀態及紙帶上的型態決定下一步，包括
改寫型態、變換狀態，且這套規則有個開始點跟結束點；狀態紀錄器註明了模型現在的狀態，以便讓機器遵
循規則進行。Turing提出的這個模型，讓機器不只能處理一個問題，而讓建造一個多功能的機器變得可能。
    '''
    
    vonNewmannModelSTR = '''von Neumann Model將機器的program部分儲存在memory。這樣操作的程序不
再是被寫死的，而是可以更改的。然而，要完成這樣的模型，program跟data就必須以相同的型式儲存在memory
裡，因此如何區分program和data就變得十分重要。
    
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
