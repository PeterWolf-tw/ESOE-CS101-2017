#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
    x=input('enter a string:\n')
    print(charFreqLister(x))

def charFreqLister(inputSTR):
    resultLIST = []
    freq = {}

    for x in inputSTR:
        freq[x] = inputSTR.count(x)
        freq[x]=  freq[x]/len(inputSTR)
    for y in freq:
        resultLIST.append((freq[y], y))

    resultLIST.sort(key=lambda input:input[0], reverse=True)

    return resultLIST


def condNOT(inputSTR_X):
    outputSTR = ""
    for i in inputSTR_X:
        if i == "0":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR


def condAND(inputSTR_X, inputSTR_Y):
    output= ""
    for (x,y) in zip(inputSTR_X,inputSTR_Y):
        if x=="1" and y =="1":
            output = output + "1"
        else:
            output = output + "0"

    return output


def condOR(inputSTR_X, inputSTR_Y):
    output = ""
    for (x,y) in zip(inputSTR_X,inputSTR_Y):
        if x=="0" and y=="0":
            output = output + "0"
        else:
            output = output + "1"

    return output


def conXOR(inputSTR_X, inputSTR_Y):
    output = ""
    for (x,y) in zip(inputSTR_X,inputSTR_Y):
        if x == "0" and y =="0":
            output = output + "0"
        elif x == "1" and y == "1":
            output = output + "0"
        else:
            output = output + "1"

    return output


if __name__=="__main__":
    main()


    condition00X = str(bin(0xE5CC)[2:])
    condition00Y = str(bin(0xCCE5)[2:])
    print(condition00X)
    print(condition00Y,end = "\n\n")
    condition01 = condNOT(condition00X)
    condition02 = condAND(condition00X,condition00Y)
    condition03 = condOR(condition00X,condition00Y)
    condition04 = conXOR(condition00X,condition00Y)
    print(condition01)
    print(condition02)
    print(condition03)
    print(condition04)


    print("Ans:")
    Ch3P3_20a = "01000000111001100000000000000000"
    Ch3P3_20b = "11000001010011100100000000000000"
    Ch3P3_20c = "01000001001101101000000000000000"
    Ch3P3_20d = "10111110110000000000000000000000"
    print("========")
    Ch3P3_28a = "234"
    Ch3P3_28b = "560"
    Ch3P3_28c = "874"
    Ch3P3_28d = "888"
    print("========")
    Ch3P3_30a = "234"
    Ch3P3_30b = "560"
    Ch3P3_30c = "875"
    Ch3P3_30d = "889"
    print("========")
    Ch4P4_3a = "10011001"
    Ch4P4_3b = "10011001"
    Ch4P4_3c = "11111111"
    Ch4P4_3d = "11111111"
    print("========")
    Ch4P4_4a = "01100110"
    Ch4P4_4b = "11111111"
    Ch4P4_4c = "00010001"
    Ch4P4_4d = "10111011"
    print("========")
    Ch4P4_13a = "0000010010100001"
    Ch4P4_13b = "1111110010100010"
    Ch4P4_13c = "0000001101011110"
    Ch4P4_13d = "1111101101011111"
    print("========")
    Ch4P4_15a = "overflow"
    Ch4P4_15b = "not overflow"
    Ch4P4_15c = "not overflow"
    Ch4P4_15d = "overflow"
    print("========")
    Ch4P4_16a = "0x0F51"
    Ch4P4_16b = "overflow"
    Ch4P4_16c = "0x8012"
    Ch4P4_16d = "overflow"