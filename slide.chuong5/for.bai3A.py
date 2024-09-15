# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:32:55 2024

@author: Tiến
"""

import random
def tao_danh_sach_ngau_nhien(min_length=20, max_length=30):
    length = random.randint(min_length, max_length)
    danh_sach = []
    for i in range(length):
        danh_sach.append(random.randint(0, 100))
    return danh_sach
danh_sach_moi = tao_danh_sach_ngau_nhien()
print(danh_sach_moi)
