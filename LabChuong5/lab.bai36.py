# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:18:05 2024

@author: Tiến
"""

tong = 0
n = 0
print("Hãy nhập vào số n: ")
n = int(input())
for i in range(1, n + 1) :
    tong += i ** 2
print("Tổng số là: ", tong)