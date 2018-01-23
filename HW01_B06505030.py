#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。

#程式無法執行。請查明「變數」的用法。
def modelPrinter(model):
    "A Turing machine is a mathematical model of computation invented by Alan Turing. It operates on an infinite memory tape that
    contains discrete message, or cells, also, it read/write the message from the tape, the machine translate this message from a
    'table', output the result based on the current state of machine. The output contains the logic how to modify the current state
    and the message on the tape."


    vonNewmannModelSTR =
    "The major difference between Turing model and von Neumann model is thet the 'table' used to translate message is an additional
    input, that is, the logic of hoe to translate the input is 'user-friendly'."

    #助教：你的程式無法執行，請修正後再上傳。


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
