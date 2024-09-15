# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:17:53 2024

@author: Tiến
"""

def tinh_tong(x, n):
  tong = 0
  MAU = 0
  for i in range(1, n+1):
    MAU += i
    tong += x**i / MAU
  return tong
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số lượng số hạng n: "))
ket_qua = tinh_tong(x, n)
print("Tổng của dãy số là:", ket_qua)