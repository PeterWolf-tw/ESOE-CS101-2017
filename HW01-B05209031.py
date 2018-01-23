#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。+
#助教：你的程式碼是直接從 github 的 source code 頁裡複製下來的。沒辦法直接執行哦。

def modelPrinter(model):
    turingModelSTR = '''
     在討論Turing Model前，我們先將電腦定義成一個數值處理器。當我們給電腦特定的數值(input)，
     電腦也將回傳出特定的數值(output)，也就是一個input對應到一個output。有了上述概念後，
     Turing Model其實就是多了一組稱之為program的input。Program是用來定義我們給定電腦的
     數值將被如何處理，因此當我們給予一樣的input，但可能因為program的不同，我們也將得到不同
     的output。總而言之，Turing Model的中心思想就是希望藉由另一組input(program)，來設計
     出數值將被如何運算。

     基於Turing Model所設計出來的機器稱之為Turing Machine，而此機器主要由四部分構成:
     (1)Tape：提供input和紀錄output。
     (2)Head：讀出Tape上的數值，也可覆寫上面的數值。
     (3)Table：用來定義Head讀出Tape上的數值後，將如何進行。
     (4)State Register：用來儲存目前終端機的狀態。
    '''

    vonNewmannModelSTR = '''
     vonNewmannModel有別於Turing Model的地方主要有兩點：
     (1)除了input/output data，program都儲存於記憶體內。而為了達到此一目的，input/output data和
        program必須是以相同得邏輯方式表達(相同的格式)。
     (2)program必須被依序的執行。也就是說program的運行必需有一定的順序，達成此一條件之後，當我們給予
        相同的input data和program後，我們將可以得到'預期'的結果。

     除了上述兩點對program的定義之外，也將電腦區分出以下五種不同的部分：
     (1)Input unit：將待處理的資料傳道記憶體。
     (2)Output unit：將處理好的資料從記憶體中取出。
     (3)Arithmetic logic unit(ALU)：執行數學的運算和判斷邏輯。
     (4)Controt unit：從主記憶體中提取指令碼。
     (5)Memory unit：儲存從input unit中傳來的待處理資料。
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
