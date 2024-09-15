# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:54:14 2024

@author: Tiến 
"""

n =int(input("Nhập vào số nguyên dương n:"))
def tinh_tong_chu_so(n):
    tong = 0
    while n>0 :
        chu_so = n % 10
        tong += chu_so
        n //= 10
    return tong
ket_qua = tinh_tong_chu_so(n)
print("Tổng các chữ số của", n,"là:", ket_qua)
