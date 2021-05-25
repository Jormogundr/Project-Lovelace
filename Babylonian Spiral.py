# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
 
def babylonian_spiral(N):
    # starting points
    x = [0, 0]
    y = [0, 1]
    
    zeros = np.zeros((1,N-2))
    
    #x = np.concatenate((x, zeros[0]), axis=0)
    #y = np.concatenate((y,zeros[0]))
    
    for i in range(1, N):
        x[i] = x[i-1] + 1
        for j in range(1, N):
            y[j] = x[j-1] + 1
            check = np.sqrt(x[i]**2 + y[j]**2)
            
            if check.is_integer():
                np.append(x, x[i])
                np.append(y, y[j])
                
    return [x, y]

# Consts
N = 10 # steps
arr = babylonian_spiral(N)
print(arr[0], arr[1])

plt.plot(arr)
