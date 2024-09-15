# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:47:01 2024

@author: Tiến
"""

import random
def tao_danh_sach_binh_phuong(min_value=18, max_value=99, so_luong=10):
    danh_sach = []
    for i in range(so_luong):
        so_thuc_ngau_nhien = random.uniform(min_value, max_value)
        danh_sach.append(so_thuc_ngau_nhien**2)
    return danh_sach
danh_sach_binh_phuong = tao_danh_sach_binh_phuong(18, 99, 10)
print(danh_sach_binh_phuong)
