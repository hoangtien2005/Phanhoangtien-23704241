# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:48:27 2024

@author: PC
"""

def tinh_tong(n):
  tong = 0
  for i in range(1, n+1):
    M = 2 * i
    tong += 1 / M
  return tong
n = int(input("Nhập số lượng số hạng n: "))
ket_qua = tinh_tong(n)
print("Tổng của dãy số là:", ket_qua)
