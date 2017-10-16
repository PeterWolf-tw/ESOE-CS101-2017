
#作業 1.
number = 0b11001  
print("number 的二進位表示法為：{0}".format(int(number)))


class HW02:
    def ch2(self):
        '''
        請將你計算出來的答案填入以下變數，助教會寫程式自動批改。
        Ch2P2_19a = "xxx"
        意思是
        Ch2   : 第二章
        P2_19a: 第二章結尾處的 PRACTICE SET 段落處的 Problems 第 P2-19 題的 a 小題
        "xxx" ： 你要填入你的答案在 xxx 這裡。
        '''
        #作業 2. 課本 Ch2. P2.19
        self.Ch2P2_19a = "10"
        self.Ch2P2_19b = "13"
        self.Ch2P2_19c = "6"
        self.Ch2P2_19d = "8"

        #作業 3. 課本 Ch2. P2.20
        self.Ch2P2_20a = "14"
        self.Ch2P2_20b = "8"
        self.Ch2P2_20c = "13"
        self.Ch2P2_20d = "4"

        #作業 4. 課本 Ch2. P2.22
        self.Ch2P2_22a = "00010001 11101010 00100010 00001110"
        self.Ch2P2_22b = "00001110 00111000 11101010 00111000"
        self.Ch2P2_22c = "01101110 00001110 00111000 01001110"
        self.Ch2P2_22d = "00011000 00111000 00001101 00001011"


    def ch3(self):
        '''
        請將你計算出來的答案填入以下變數，助教會寫程式自動批改。
        Ch3P3_28a = "xxx"
        意思是
        Ch3   : 第三章
        P3_28a: 第三章結尾處的 PRACTICE SET 段落處的 Problems 第 P3-28 題的 a 小題
        "xxx" ： 你要填入你的答案在 xxx 這裡。
        '''
        #作業 5. 課本 Ch3. P3.28
        self.Ch3P3_28a = "0 10000001 11001100000000000000000"
        self.Ch3P3_28b = "0 10000010 01101101000000000000000"
        self.Ch3P3_28c = "1 10000010 10010100100000000000000"
        self.Ch3P3_28d = "1 10111101 10000000000000000000000"

        #作業 6. 課本 Ch3. P3.30
        self.Ch3P3_30a = "766"
        self.Ch3P3_30b = "440"
        self.Ch3P3_30c = "125"
        self.Ch3P3_30d = "111"
        
        
   if __name__ == '__main__': #程式進入點，程式由此行開始執行。以下示範助教的批改程式。
    checkHW02 = HW02()
    checkHW02.ch2()
    if checkHW02.Ch2P2_19a == "10": #10 是這題的正解。此行檢查這題的答案。
        print("Ch2P2_19a:{0}".format("Correct!"))
    else:
print("Ch2P2_19a:{0}".format("Incorrect!"))



