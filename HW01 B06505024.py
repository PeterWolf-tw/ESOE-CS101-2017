#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01
#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。
#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。

def modelPrinter(model):
    turingModelSTR = ''' 1. 1936年Alen Turing 提出一個universal computational device(通用計算設備), 
    稱為Turing machine, Turing 認為所有的計算都可以用Turing Machine來完成。2.根據Turing Model的一個計
    算機程式:一系列的指令告訴計算機如何操作在input data上, output data是由程式運作在 input data而得到。
     3.turing machine只是抽象的理論model, 並不是真實的computer, 但這理論的model被用來證明了一個問題
     (Halting problem)是 Turing machine沒辦法解的,因此也是今日的computer沒辦法解的 4.今日的computer計
     算能力與Turing Machine完全一樣, 所以Turing Machine可以完全的描述今日computer的計算
    能力。 
    '''        
    vonNewmannModelSTR = '''   
    馮·紐曼模型（Von Neumann model)，是一種將程式指令記憶體和資料記憶體合併在一起的電腦設計概念架構。本詞描述的
    是一種實作通用圖靈機的計算裝置，以及一種相對於平行計算的序列式架構參考模型（referential model）。本架構隱約
    指導了將儲存裝置與中央處理器分開的概念， 因此依本架構設計出的計算機又稱儲存程式電腦。    

    
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
