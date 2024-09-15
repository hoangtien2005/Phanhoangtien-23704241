# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:34:43 2024

@author: Tiến 
"""

def liet_ke_nghiem(a, b, c, d):
    for x in range(1, d//a +1):
      for y in range(1, (d - a*x)//b + 1):
        z = (d - a*x - b*y) //c
        if z>0 and (a*x + b*y + c*y) == d:
            print(f"Nghiệm: (x={x}, y={y}, z={z})")
