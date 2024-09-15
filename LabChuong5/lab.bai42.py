# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:01:50 2024

@author: Tiến 
"""

n=int(input('n='))
S=0
for i in range (1,n+1):
 S+=i*(i+1)
print('Tổng S là:',S)