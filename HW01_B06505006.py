#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = "圖靈機是一種理想的計算設備，和一般只能把輸入的資料做特定處理的「計算器」不同，圖寧機強調「程式」的運用。藉由程式，圖寧機可以將輸入的資料作不同的處理，而不是只有一項功能。圖寧機包括讀寫頭和通過它的磁帶。該磁帶是機器的存儲位置，用作輸入和輸出的載具，並且用於記錄計算過程中間步驟的結果的記憶體。在計算開始之前刻錄在磁帶上的輸入必須由有限的符號組成。然而，磁帶是無限長的，因為圖靈的目的是想證明這些機器無法執行某些任務，即便給予無限記憶體和時間。"

    vonNewmannModelSTR = "馮·諾依曼模型是基於儲存計算程序的概念，並將計算機硬體分為四個子系統：算術邏輯元件(ALU)，記憶體，控制元件和輸入/輸出。算術邏輯元件執行運算和邏輯(AND，OR，NOT)的操作。記憶體內含一組程序及其相應的資料，因此他們應以相同的格式儲存控制元件控制計算機的ALU，記憶體和輸入/輸出的操作，告訴他們如何對從記憶體讀取和解釋的程序指令進行回應。控制元件還提供其他計算機組件所需的定時和控制信號。"

    #可以用三個單或雙引號 ''' or """ 包夾起來的字串，就可以控制換行了。

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