#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''
    Turing Model，模仿人類進行數學計算，解決任何有限數學問題的模型。
    其組成包含：
    有限集合Q，包含了整個運算過程中所有可能狀態
    有限集合Σ，包含了所有可能輸入且不能為空白
    無限序列Γ，為Σ加上空白，代表所有能處理的資料
    轉移函數δ
    起始狀態Q0
    接受狀態Qa
    停止狀態Qr
    其中Q0、Qa、Qr屬於Q且Qa不等於Qr。

    機器開始時會在序列Γ上Q0的位置，依據δ決定執行的動作並在序列Γ上移動
    若流程進入了狀態Qa(Qr)則流程中斷，得一輸出結果並準備(拒絕)接受外部輸入
    
    '''
    
    vonNewmannModelSTR = '''
    von Newmann Model，一種將程式指令與資料一同紀錄的通用圖靈機架構，將運算程式分割為一連串指令，並將指令作為一種特殊的靜態資料，使程式的編寫與變更可以極具彈性。
    其組成包含：
    紀錄資料的記憶體
    控制流程的控制單元
    專精於運算的算術單元
    控制資料輸出輸入的輸出輸入單元

    工作開始時IO單元將資料輸入運算單元
    運算單元將資料寫入記憶體
    控制單元根據記憶體中的程式執行一連串指令控制算術單元進行運算
    運算單元處理來自記憶體及IO單元的資料，並視指令決定將處理後的資料寫回記憶體或透過IO單元輸出
    '''
    
    if model == "Alen Turing":
        print(turingModelSTR)
        print("共計"+str(len(turingModelSTR))+"字符")
    elif model == "von Newmann":
        print(vonNewmannModelSTR)
        print("共計"+str(len(vonNewmannModelSTR))+"字符")
    else:
        pass
        
        
if __name__ == "__main__":
    modelPrinter("Alen Turing")
    print("=====我是分隔線=====")
    modelPrinter("von Newmann")




