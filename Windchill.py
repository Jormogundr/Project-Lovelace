# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:26:40 2021

@author: Nate
"""


def wind_chill(T, w):
    term1 = 13.12
    term2 = 0.6215*T
    term3 = 11.37*w**0.16
    term4 = 0.3965*T*w**0.16
    return term1 + term2 - term3 + term4

print(wind_chill(-25,30))