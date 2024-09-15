# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:16:16 2024

@author: Tiến
"""

x = float(input("nhập số:"))
while x > -99 or x < 99:
    x = float(input(" nhập lại số: "))
    print ("giá trị đã nhập:", x)