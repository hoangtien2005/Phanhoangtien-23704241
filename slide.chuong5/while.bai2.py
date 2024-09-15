# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:21:27 2024

@author: Tiến 
"""

while True:
    try:
        gia_tri = float(input("Nhập giá trị (trong khoảng [-89.9, 88.8]): "))
        if -89.9 <= gia_tri <= 88.8:
            print(f"Giá trị hợp lệ: {gia_tri}")
            break 
        else:
            print("Giá trị không hợp lệ. Vui lòng nhập lại.")
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập một số thực.")