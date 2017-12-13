#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def modelPrinter(model):
    turingModelSTR = '圖林機是一種模仿人類計算模式的機器，任何人類可以計算的過程皆可由圖林機進行處理。圖林機進行計算需要包含兩種輸入，分別是資料和程式，由不同的程式處理相同一組資料會得到不同的輸出資料。而圖林機也被稱作為數學邏輯機，因為他在做計算的時候就是在做邏輯的運算，圖林的模型以紙帶呈現，邏輯判斷決定寫上符號或擦除符號，以及下一步要向右向左或不動，由此得到一串編碼就是圖林機的輸出。廣用圖林機則是現代電腦的原型，藉由提供不同的資料和程式，廣用圖林機可以做任何一種計算，它能接收任何圖林機的編碼並且模仿此圖林機來運算。'
    
    vonNewmannModelSTR = '馮紐爾曼的模型與圖林機最大的差別在於馮紐爾曼認為資料與程式輸入的邏輯是相同的，因此資料與程式應被一同儲存於電腦的記憶體裡面，並以相同的編碼方式做儲存，儲存的編碼是用二進位的形式。硬體方面分成四個部分分別是：記憶體、控制中心、輸入輸出以及計算邏輯元件。至於程式的執行，由控制中心照順序從記憶體中解碼指令並執行。'
    
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