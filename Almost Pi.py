# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:18:35 2021

@author: Nate
"""

import matplotlib.pyplot as plt
import numpy as np

def almost_pi(N):
    p = 0
    arr = []
    for k in range(0, N):
        num = (-1)**k
        denom = 2*k + 1
        p += num/denom
        arr.append(4*p)
        plt.plot(arr, linewidth=1)
        
        
    return 4*p

n = 100
x = np.linspace(0, n, n)
y = [np.pi]*n

plt.ylabel('Sum')
plt.plot(x, y, label='pi', linewidth=2, color='tab:red')
plt.legend()
print(almost_pi(n))
plt.show()