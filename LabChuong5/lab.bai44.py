# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:12:30 2024

@author: Tiến
"""

def tinh_tong(n):
  tong = 0
  for i in range(1, n+1):
    TU = 2*i - 1
    MAU = 2*i
    tong += TU / MAU
  return tong
n = int(input("Nhập số lượng số hạng n: "))
ket_qua = tinh_tong(n)
print("Tổng của dãy số là:", ket_qua)