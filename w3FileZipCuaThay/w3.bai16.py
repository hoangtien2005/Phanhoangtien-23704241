# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:17:03 2024

@author: Tiến
"""

n = input("Nhập một số nguyên dương: ")
while True:
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
        else:
            print("Số nguyên phải lớn hơn 0. Vui lòng nhập lại:")
    else:
        print("Vui lòng nhập một số nguyên hợp lệ:")
    n = input()
A = bin(n)[2:]
print("Biểu diễn nhị phân của số là:",A)