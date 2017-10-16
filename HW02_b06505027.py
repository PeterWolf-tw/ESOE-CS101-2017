def int2bin(N):
    M = N
    tmpLIST = []
    while N > 0:
        remainder = int(N % 2)
        tmpLIST.append(remainder)
        N = (N - remainder) / 2
    tmpLIST.append(0)

    ans = ""
    for j in tmpLIST[::-1]: #將 tmpLIST 中的數字從尾至頭傳入 j
        ans = ans + str(j)
    print("{0} 的二進位表示為 {1}.".format(M, ans))
    return None

def bin2int(N):
    L = int(len(str(N)))
    A = 0
    K = 0
    while L > K:
        r = int(N % 10)
        A = A + 2**(K) * r
        N = N / 10
        K = K + 1
        
    str(A)
    return A

class HW02:
    def ch2(self):
        self.Ch2P2_19a = '10'
        self.Ch2P2_19b = '17'
        self.Ch2P2_19c = '6'
        self.Ch2P2_19d = '8'
        
        self.Ch2P2_20a = '15'
        self.Ch2P2_20b = '9'
        self.Ch2P2_20c = '14'
        self.Ch2P2_20d = '5'
        
        self.Ch2P2_22a = '00010001 11101010 00100010 00001110'
        self.Ch2P2_22b = '00001110 00111000 11101010 00111000'
        self.Ch2P2_22c = '01101110 00001110 00111000 01001110'
        self.Ch2P2_22d = '00011000 00111000 00001101 00001011'        
    
    def ch3(self):
        self.Ch3P3_28a = "234"
        self.Ch3P3_28b = "overflow"
        self.Ch3P3_28c = "874"
        self.Ch3P3_28d = "888"

        self.Ch3P3_30a = "234"
        self.Ch3P3_30b = "overflow"
        self.Ch3P3_30c = "875"
        self.Ch3P3_30d = "889"
        
        
if __name__ == '__main__': #程式進入點，程式由此行開始執行。以下示範助教的批改程式。
    checkHW02 = HW02()
    checkHW02.ch2()
    if checkHW02.Ch2P2_19a == "10": #10 是這題的正解。此行檢查這題的答案。
        print("Ch2P2_19a:{0}".format("Correct!"))
    else:
        print("Ch2P2_19a:{0}".format("Incorrect!"))