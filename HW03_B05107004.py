#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2016.10.17

# 作業內容：
# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。


if __name__== "__main__":
    inputSTR=input("input something")#取得輸入字串
    result=""#宣告編碼結果為字串
    class node:#建立node類別
        def __init__(self,char,freq,left=None,right=None,father=None):#建構以下實體屬性
            self.char=char
            self.freq=freq
            self.left=left
            self.right=right
            self.father=father

    #def charFreqLister(inputSTR):
        #resultLIST =[]
        #freq = {}
        #for x in inputSTR:
            #freq[x] = inputSTR.count(x)
            #freq[x]=  freq[x]/len(inputSTR)
        #for y in freq:
            #resultLIST.append((freq[y], y))
        #resultLIST.sort(key=lambda input:input[0], reverse=False)
        #return resultLIST

    #charFreqLister(inputSTR)
# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
#reference to http://blog.game18.net/posts/2016/05/huo-fu-man-bian-ma/
    def huffmanTranslater(inputSTR):#實作霍夫曼解編碼器


        ResultList=[]#儲存字數統計結果
        nodelist=[]#儲存二元樹
        def freqanalysis(inputSTR):#為避免浮點數及過多全域變數，拋棄charFreqLister並重新實作字數統計
            ResultDict={}#將字數記入字典
            for c in inputSTR:#走訪intputSTR
                if c in ResultDict.keys():#若目前字元已在字典中有項目
                    ResultDict[c]+=1#則該項目計數+1
                else:#否則
                    ResultDict[c]=1#新增該項目並將計數設為1

            #將字典的(key:value)轉換成('字元',字數)形式存入list以便排序
            for c in ResultDict.keys():#走訪ResultDict
                ResultList.append((c,ResultDict[c]))#依序存入ResultList
            #輸出字數統計結果
            i=0
            while i < len(ResultList):
                print(ResultList[i])
                i=i+1
            #結束字數統計
        def MakeHuffTree(ResultList):#建立霍夫曼樹
            for element in ResultList:#走訪ResultList
                nodelist.append(node(element[0],element[1]))#將'字元'存入節點的char屬性，將頻率存入節點的freq屬性
            while len(nodelist)>1:#重複此流程直到頻率列表中剩下一個節點
                nodelist.sort(key=lambda element:element.freq)#依照頻率對節點由低到高排序
                leftnode=nodelist.pop(0)#移除最小的節點並設為左子節點
                rightnode=nodelist.pop(0)#移除次小(現為最小)的節點並設為右子節點
                fathernode=node(leftnode.char+rightnode.char,leftnode.freq+rightnode.freq,leftnode,rightnode)#建構父節點合併freq值並連接兩個子節點
                leftnode.father=fathernode#將左子節點連接父節點
                rightnode.father=fathernode#將右子節點連接父節點
                nodelist.append(fathernode)#向根新增父節點至樹上
            #結束建立霍夫曼樹
        def HuffEncoder(char,tree):#實作編碼器
            code=""#宣告code為字串以儲存編碼
            while tree.left:#如果當前節點存在左節點(因霍夫曼樹為complete binary tree，亦即當前節點非終端節點)

                if char in tree.left.char:#如果找尋字元過程中經過一次左子節則編碼多一個'0'
                    code+='0'#在編碼加上'0'
                    tree=tree.left
                else:#如果找尋字元過程中經過一次右子節則編碼多一個'1'
                    code+='1'#在編碼加上'1'
                    tree=tree.right
            return code

        def encode(char,codes):#給定一連串字元與字典，參照字典將字元編碼結果輸出
            global result#保持result為全域變數

            for c in char:#走訪輸入字串並取出字元
                result+=codes[c]#按字典將對應編碼接上輸出





        def decode(code,tree):#實作解碼器
            CurrentNode=tree#設定初始化當前節點為根
            s=""#宣告s為字串
            for c in code:#走訪霍夫曼碼
                if c=='0':#如果讀數為'0'
                    if CurrentNode.left.left:#且當前節點的左子節點有左子節點
                        CurrentNode=CurrentNode.left#則將左子節點設為當前節點(向左走)
                    else:#且當前節點的左子節點為終端節點
                        s+=CurrentNode.left.char#則將該終端節點之'字元'接上s
                        CurrentNode=tree#當前節點回到樹根
                else:#如果讀數為1
                    if CurrentNode.right.right:#且當前節點的右子節點有右子節點
                        CurrentNode=CurrentNode.right#則將右子節點設為當前節點(向右走)
                    else:#且當前節點的右子節點為終端節點
                        s+=CurrentNode.right.char#則將該終端節點之'字元'接上s
                        CurrentNode=tree#當前節點回到樹根
            print(s)#輸出s
            return s
        freqanalysis(inputSTR)#呼叫freqanalysis對inputSTR進行分析
        MakeHuffTree(ResultList)#呼叫MakeHuffTree參照分析結果建立霍夫曼樹
        #建立字典儲存所有字符以及對應的編碼
        codes={}

        for element in ResultList:#走訪ResultList
            codes[element[0]]=HuffEncoder(element[0],nodelist[0])#呼叫HuffEncoder對ResultList一一進行編碼並將編碼結果連同原始字符以字符為key，編碼為value形式對應至字典
        print(codes)#輸出對應情形
        #結束字典建立
        encode(inputSTR,codes)#呼叫encode對inputSTR參照字典進行編碼
        print(result)#輸出霍夫曼碼
        decode(result,nodelist[0])#呼叫decode對霍夫曼碼進行解碼並輸出
    huffmanTranslater(inputSTR)#呼叫huffTranslater對inputSTR進行編碼與解碼




# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

#condition00 not condition01
    def condNOT(inputSTR_X):
        outputSTR =""
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







	#condition00X = ""
    #condition00Y = ""

    #condition01 = condNOT(condition00X)
    #print(condition01)

    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    # Ch3 表示為第三章
    # P3_20a 表示為該章最後 Problem 處的 P3-20 題的第 a 小題。
    print("Ans:")
    Ch3P3_20a = "0 10000001 000 0000 0000 0000 0011 0011"
    Ch3P3_20b = "1 10000010 000 0000 0000 0001 0010 1001"
    Ch3P3_20c = "0 10000010 000 0000 0000 0000 0110 1101"
    Ch3P3_20d = "1 01111101 000 0000 0000 0000 0000 0001"
    print("========")
    Ch3P3_28a = "234"
    Ch3P3_28b = "overflow"
    Ch3P3_28c = "874"
    Ch3P3_28d = "888"
    print("========")
    Ch3P3_30a = "235"
    Ch3P3_30b = "overflow"
    Ch3P3_30c = "875"
    Ch3P3_30d = "889"
    print("========")
    Ch4P4_3a = "0x99"
    Ch4P4_3b = "0x99"
    Ch4P4_3c = "0xFF"
    Ch4P4_3d = "0xFF"
    print("========")
    Ch4P4_4a = "0x66"
    Ch4P4_4b = "0xFF"
    Ch4P4_4c = "0x11"
    Ch4P4_4d = "0xBB"
    print("========")
    Ch4P4_13a = "1184"
    Ch4P4_13b = "-862"
    Ch4P4_13c = "862"
    Ch4P4_13d = "-1184"
    print("========")
    Ch4P4_15a = "X"
    Ch4P4_15b = "X"
    Ch4P4_15c = "X"
    Ch4P4_15d = "O"
    print("========")
    Ch4P4_16a = "0xF51"
    Ch4P4_16b = "overflow"
    Ch4P4_16c = "0x8012"
    Ch4P4_16d = "overflow"