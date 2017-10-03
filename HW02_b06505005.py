#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def bin2int(N):
    n = int(input(N))
    A = 0
    I = 0

if __name__ == "__main__" :

while n >= 0:
     remainder = n % 2
     n = (n - remainder) / 10
     A += remainder * 2**I
     I = I + 1
     ans = A
     

      print("{N} 的二進位表示為 {A}.".format(N, ans))
