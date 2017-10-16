@@ -0,0 +1,51 @@
 +#!/usr/bin/env python3
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
 +    turingModelSTR = Turing Model(Machine)是一台假想的機器，由Alan Turing提出，以模擬人們用紙筆進行數學運算的過程。
 +    機器主要分成四個部分：
 +    1.一條無限長的紙帶：上面被劃分成無限個小格子，每個格子上面會有一個符號
 +    2.一個讀寫頭：能在紙上左右移動、讀出當前格子上的符號、及改變當前格子上的符號
 +    3.一套控制規則：根據狀態暫存器定義的狀態和當前讀寫頭指到格子上的符號來決定下一步動作
 +    4.一個狀態暫存器：儲存當前機器所處的狀態
 +    機器運作時會用讀寫頭在紙帶上讀出一個格子的資訊，根據它當前的內部狀態開始對程式進行查表，
 +    然後得出一個輸出動作，也就是是否在紙帶上寫入或改變資訊，還是移動讀寫頭到下一個格字，同時也會告訴它下一時刻內部狀態轉移到哪一個。
 +
 +    
 +    '''
 +    
 +    vonNewmannModelSTR = Von Newmann Model是一種將程式指令記憶體和數據記憶體合併在一起的電腦設計概念模型，也就是內存程式（Stored Program）的概念，
 +    簡單來說，就是使用記憶體來儲存計算機的指令與資料。
 +    以往的計算機器僅含有固定用途的程式，而von Newmann提出的概念，則藉由創造一組指令集架構，將運算轉化成一串程式指令的執行細節，
 +    讓此機器更有彈性。藉著將指令當成一種特別型態的靜態資料，一台儲存程式型電腦可輕易改變其程式，並在程式控制下改變其運算內容。
 +    此理論模型分為五大架構：
 +    1.控制單元 Control Unit
 +    2.算術與邏輯單元 Arithmetic Logic Unit
 +    3.記憶單元 Memory Unit
 +    4.輸入單元 Input Unit
 +    5.輸出單元 Output Unit
 +    
 +    '''
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
