# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:57:00 2024

@author: Tien
"""

so_km = float(input("Nhập số km di chuyển: "))
tong_tien = 0
if so_km <= 0:
 if so_km <= 1:
    tong_tien += 15000
 elif so_km <= 5:
    tong_tien = 15000 + (so_km - 1) * 13500
else:
    tong_tien = 15000 + 4 * 13500 + (so_km - 5) * 11000

if so_km > 120:
    tong_tien *= 0.9  # Giảm 10%   
tien_phai_tra = tong_tien
print("Tổng số tiền phải trả là:", tien_phai_tra, "đồng")