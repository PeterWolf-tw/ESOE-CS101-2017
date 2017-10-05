#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
    print("第 5 行")
    x = 1
    y = 2
    print(myAdder(x, y))
    print(plusOne(x, y))
def plusOne(inputX, inputY):
    inputX = inputX + 1
    inputY = inputY + 1
    z = bigger(inputX, inputY)
    return ("兩者的和是：", myAdder(inputX, inputY), "其中", z, "比較大。")

def myAdder(inputX, inputY):
    return (inputX+inputY)

def bigger(inputX, inputY):
    if inputX > inputY:
        return inputX
    elif inputX < inputY:
        return inputY
    else:
        return None

if __name__== "__main__":
    print("第 9 行")
    main()