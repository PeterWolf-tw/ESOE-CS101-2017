
Type "copyright", "credits" or "license()" for more information.
>>> def modelPrinter(model): '''一台為了模仿人的運算過程的假想機器，首先分成4個部分，第一個是無限長的紙帶(tape)
    分成無限多個格子，其中每個格子上都有一個符號，第二個則是讀寫頭(head)，它能讀出當前所在格子中的符號並對此
    當前符號做出改變，第三個是一套運算規則(table)，這規則能告訴讀寫頭該做什麼事以及接下來要做的事，最後一個則
    是狀態儲存器，負責儲存目前的狀態，狀態儲存器只能保存有限個狀態。在運算過程中首先把符號串由左填至紙帶的格子
    中，依照狀態機中的狀態，讀寫頭去讀當前的符號並依照運算規則決定下一步該如何，運算完之後更新狀態機的狀態，並
    持續接下來的步驟。
    
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
