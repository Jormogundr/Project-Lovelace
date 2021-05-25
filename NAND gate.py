# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:41:37 2021

@author: Nate
"""

# Input: Two integers A and B that have the value 0 or 1.
# Output: The output of a NAND gate with inputs A and B.

def NAND(A, B):
    if A == 1 and B == 1: return 0
    else: return 1
    
if __name__ == '__main__':
    A = 1
    B = 0
    print(NAND(A,B))
    