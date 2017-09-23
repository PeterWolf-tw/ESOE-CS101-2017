Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def modelPrinter(model):
    turingModelSTR = '''Turing model是利用機器進行計算的一個想法。Turing machine分成幾個部分¬¬–紙帶、讀寫頭、控制規則、狀態暫存器。紙帶上有一格格的空格，空格裡寫了一個符號，由讀寫頭讀出符號後，控制規則決定讀寫頭的動作，可能是修改空格裡的數字或是移到其他格來進行計算，最後則是狀態暫存器。
    
    '''
    
    vonNewmannModelSTR = '''vonnewmann model是等同於把好多個turing machine合在一起。跟turing machine一起來比較，vonnewmann model多了一條有控制規則的紙帶使得她變得多元化，原本要不同台才能做的事，現在一台就可以。
    
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
