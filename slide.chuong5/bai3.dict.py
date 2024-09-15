# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:48:39 2024

@author: Tiến
"""

n = int(input("Nhập giá trị nguyên n: "))
dsach = {}
for i in range(1, n + 1):
    dsach[i] = i ** i
print("Dictionary vừa tạo là:")
print(dsach)