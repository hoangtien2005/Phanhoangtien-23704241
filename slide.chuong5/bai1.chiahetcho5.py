# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:23:36 2024

@author: Tiến
"""

danhsachchiahetcho5 = []
for num in range(2018, 2829):
    if num % 2 == 0 and num % 5 == 0:
        danhsachchiahetcho5.append(num)
print("Danh sách các số chẵn chia hết cho 5 từ 2018 đến 2828:")
for number in danhsachchiahetcho5:
    print(number)