# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:34:04 2024

@author: Tiến
"""

n = 123456789
m = 0
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10
    print("m=",m,"n=",n)