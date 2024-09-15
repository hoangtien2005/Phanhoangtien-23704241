# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:51:07 2024

@author: Tiến
"""

while True:
    n = input("Nhập giá trị của n: ")
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương.")
    else:
        print("Vui lòng nhập một số nguyên hợp lệ.")
power_of_two = 1
while power_of_two <= n:
    print(power_of_two)
    power_of_two *= 2