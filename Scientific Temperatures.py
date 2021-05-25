# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:19:48 2021

@author: Nate
"""

def fahrenheit_to_celsius(F):
    factor = 5/9
    return factor*(F-32)

if __name__ == '__main__':
    c = fahrenheit_to_celsius(17)
    print(c)