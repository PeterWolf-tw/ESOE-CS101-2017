


def modelPrinter(model):
    turingModelSTR = '''Turing Model 的基本概念是用機器來模擬人類進行數學運算的過程,由一個無限長的紙帶用來記錄資料
一個讀寫頭用來讀取或改寫資料,一套特定的運算規則,一個暫存器用來紀錄Turing Model當時的狀態。'''
    
    vonNewmannModelSTR = '''將Turing Model中的運算規則也視為一串資料，可被修改儲存，
使vonNewmannModel不像Turing Model只有單一功能 '''
    
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
