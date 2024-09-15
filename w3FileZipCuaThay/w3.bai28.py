# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:35:03 2024

@author: Tiến 
"""

m = input("Nhập số nguyên m : ")
n = input("Nhập số nguyên n: ")
while True:
    if m.lstrip('-').isdigit() and n.lstrip('-').isdigit():
        m = int(m)
        n = int(n)
        if m > 0 and n > 0:
            break
        else:
            print("Cả hai số nguyên phải lớn hơn 0. Vui lòng nhập lại:")
    else:
        print("Vui lòng nhập các số nguyên hợp lệ:")
    m = input("Nhập số nguyên m: ")
    n = input("Nhập số nguyên n: ")
a, b = m, n
while b != 0:
    a, b = b, a % b
print("Ước chung lớn nhất của {} và {} là: {}".format(m, n, a))