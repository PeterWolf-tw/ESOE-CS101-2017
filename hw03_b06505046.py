#缺乏檔頭

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


#condition00 and condition02
def condAND(inputSTR_X, inputSTR_Y):
    output= ""
    for (x,y) in zip(inputSTR_X,inputSTR_Y):
        if x=="1" and y =="1":
            output = output + "1"
        else:
            output = output + "0"


    return output

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    output = ""
    for (x,y) in zip(inputSTR_X,inputSTR_Y):
        if x=="0" and y=="0":
            output = output + "0"
        else:
            output = output + "1"




    return output

#condition00 xor condition04
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



if __name__== "__main__":
    condition00X = ""
    condition00Y = ""

    condition01 = condNOT(condition00X)
    print(condition01)


    print("Ans:")
    Ch3P3_20a = "0100 0000 1110 0110 0000 0000 0000 0000"
    Ch3P3_20b = "1100 0001 0100 1010 0100 0000 0000 0000"
    Ch3P3_20c = "0100 0001 0011 0110 1000 0000 0000 0000"
    Ch3P3_20d = "1011 1110 1100 0000 0000 0000 0000 0000"
    print("========")
    Ch3P3_28a = "765"
    Ch3P3_28b = "439"
    Ch3P3_28c = "overflow"
    Ch3P3_28d = "overflow"
    print("========")
    Ch3P3_30a = "766"
    Ch3P3_30b = "440"
    Ch3P3_30c = "overflow"
    Ch3P3_30d = "overflow"
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
    Ch4P4_13a = "1184"
    Ch4P4_13b = "-862"
    Ch4P4_13c = "862"
    Ch4P4_13d = "-1184"
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