# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:42:17 2024

@author: Tiến
"""

danhsachsochan = []
for num in range(2020, 3839):
    if num % 2 == 0:
        danhsachsochan.append(num)
chiahet9 = []
for number in danhsachsochan:
    if number % 9 == 0:
        chiahet9.append(number)
print("Danh sách các số chia hết cho 9:")
output = ""
for number in chiahet9:
    output += str(number) + "\t"
output = output.rstrip("\t")
print(output)