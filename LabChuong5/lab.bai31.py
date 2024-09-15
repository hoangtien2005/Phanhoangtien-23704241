# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:50:32 2024

@author: Tien
"""

A = int(input("Nhập cạnh A: "))
B = int(input("Nhập cạnh B: "))
C = int(input("Nhập cạnh C: "))
if A <= 0 or B <= 0 or C <= 0:
    print ("Không phải là tam giác")
if A + B <= C or B + C <= A or C + A <= B:
    print ("Không phải là tam giác")
if A == B == C:
    print ("Tam giác đều")
elif A == B or B == C or C == A:
    print ("Tam giác cân")
elif A**2 + B**2 == C**2 or B**2 + C**2 == A**2 or C**2 + A**2 == B**2:
    print ("Tam giác vuông")
else:
    print( "Tam giác thường")