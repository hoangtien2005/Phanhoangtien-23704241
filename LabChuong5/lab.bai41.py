# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:59:10 2024

@author: 
"""

def tinh_tong(n):
  tong = 0
  for i in range(n+1):
    M = 2*i + 1
    tong += 1 / M
  return tong
n = int(input("Nhập số lượng số hạng n: "))
ket_qua = tinh_tong(n)
print("Tổng của dãy số là:", ket_qua)
