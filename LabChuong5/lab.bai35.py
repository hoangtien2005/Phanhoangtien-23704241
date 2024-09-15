# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:34:00 2024

@author: Tien
"""

def tinh_tong(n):
 S = 0
 for i in range(1, n+1):
    S += i
 return S
n = int(input("Nhập vào số nguyên dương n: "))
ket_qua = tinh_tong(n)
print("Tổng S = 1 + 2 + ... + là", ket_qua)