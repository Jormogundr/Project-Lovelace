# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:06:24 2021

@author: Nate
"""

def compound_interest(m, r, n):
    arg = 1 + r
    exp = arg**n
    return m*exp
    

input1 = [1000, 0.07, 25]

print(compound_interest(*input1))