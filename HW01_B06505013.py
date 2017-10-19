#!/usr/bin/env python3
 +# -*- coding:utf-8 -*-
 +
 +
 +#Chapter 01
 +
 +#第 01 題
 +#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。
 +
 +#第 02 題
 +#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。
 +
 +
 +def modelPrinter(model):
 +    turingModelSTR = '''Turing machine的基本概念是模擬人進行數學運算的過程，包含三個部分：無限長的紙帶(TAPE)
、讀寫頭(HEAD) 、控制規則(TABLE) 。紙帶被劃分為無數小格子，每個格子上記載著不同符號，可看作運算的輸入及輸出。讀寫
頭可讀取紙帶上當下所指的符號。控制規則則可根據機器當下所處的狀態以及讀寫頭格子上所寫的符號，並給予讀寫頭移動的依據
，不論是停止運算或是移動到下一個符號。移動至下一個符號之後，重複前一步動作，做輪迴運算直到停止。人們藉由改變控制規
則，使Turing machine進行不同的運算。'''
 +    
 +    vonNewmannModelSTR = '''Von Neumann machine是Universal Turing machine的一種應用，它比Turing machine的
進步點在於表示將儲存裝置與處理器分開的概念。Von Neumann machine分為五個部分：記憶體、算術符號、控制規則、輸入及輸
出(紙帶)、讀寫頭，記憶體可儲存控制規則、輸入、輸出，而此控制規則的紀錄方式和輸入及輸出相同，才可同時記錄在Von Neum-
ann machine中，並讓讀寫頭讀取。Turing machine只可進行相同動作，而Von Neumann machine因為記錄著不同的控制規則，可
進行多種動作。由於控制規則的運行遵循一定條件，所以相同輸入搭配相同控制規則可得到相同的輸出，而不同輸入搭配不同控制規
則，得到可預期的輸出。'''
 +    
 +    if model == "Alen Turing":
 +        print(turingModelSTR)
 +    elif model == "von Newmann":
 +        print(vonNewmannModelSTR)
 +    else:
 +        pass
 +        
 +        
 +if __name__ == "__main__":
 +    modelPrinter("Alen Turing")
 +    print("=====我是分隔線=====")
 +    modelPrinter("von Newmann")
