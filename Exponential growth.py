# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:05:33 2021

@author: Nate
"""

# Input: Initial value , growth rate , time step , and number of iterations.
# Output: The numerical solution.
def exponential_growth(x0, k, dt, N):
    arr = []
    arr.append(x0)
    
    for n in range(0, N):
        xn_next =   arr[n] + k*arr[n]*dt
        arr.append(xn_next)
    return arr
    
if __name__ == '__main__':
    x0 = 5
    k = 1 
    dt = 0.6 
    N = 3
    x = exponential_growth(x0, k, dt, N)
    print(x)