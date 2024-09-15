# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:19:58 2024

@author: Tiến
"""

import math
def in_bang_gia_tri(n_list):
    print("n\tlog2(n)\tn*log2(n)\tn^2\tn^3")
    for n in n_list:
        log_n = math.log2(n)
        print(f"{n}\t{log_n:.2f}\t{n*log_n:.2f}\t{n**2}\t{n**3}")
n_value = [2, 4, 8, 16, 32, 64, 128]
in_bang_gia_tri(n_value)


            