# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:30:36 2024

@author: Tiến
"""

while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập số nguyên dương.")
    except ValueError:
        print("Vui lòng nhập số nguyên.")
print("Các ước số của", n, "là:")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")