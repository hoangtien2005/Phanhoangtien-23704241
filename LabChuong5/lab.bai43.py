# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:04:24 2024

@author: Tiến
"""

n=int(input("Nhập số n: "))
s=0
for i in range(0,n):
    s+=1/(i+1)
print("Kết quả:",s)