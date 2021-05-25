# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:55:46 2021

@author: Nate

Input: A list of temperatures in degrees Celsius.

Output: The average temperature, and the temperaure standard deviation.

"""

import numpy as np

def mean(T):
    t = 0
    N = len(T)
    for n in range(0, N):
        t += T[n]
    return t/N

def std(T, mu):
    t = 0
    N = len(T)
    for n in range(0, N):
        t += (T[n] - mu)**2
    return np.sqrt(t/N)
    

def temperature_statistics(T):
    mu = mean(T)
    sigma  = std(T, mu)
    return mu, sigma



temperatures = [4.4, 4.2, 7.0, 12.9, 18.5, 23.5, 26.4, 26.3, 22.5]
print(temperature_statistics(temperatures))