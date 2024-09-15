# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:20:16 2024

@author: Tiến 
"""

n = int(input("Nhập n: "))
S = 0 ;
for i in range(1,n+1):
    if i % 2 == 0: S += i ;
print("Tổng là: ",S)

