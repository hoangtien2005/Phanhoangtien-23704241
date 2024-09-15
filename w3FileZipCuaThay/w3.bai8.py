# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:03:04 2024

@author: Tiến
"""

import random
def tinh_thong_ke_so_ngau_nhien(n):
    tong = 0
    min_value = 1
    max_value = 0
    for i in range(n):
        so_ngau_nhien = random.random()
        tong += so_ngau_nhien
        min_value = min(min_value, so_ngau_nhien)
        max_value = max(max_value, so_ngau_nhien)
    trung_binh = tong / n
    print(f"Giá trị trung bình: {trung_binh:.2f}")
    print(f"Giá trị nhỏ nhất: {min_value:.2f}")
    print(f"Giá trị lớn nhất: {max_value:.2f}")
n = int(input("Nhập số lượng ngẫu nhiên: "))
    