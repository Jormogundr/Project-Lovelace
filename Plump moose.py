# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:38:59 2021

@author: Nate
"""

# Constants
a = 2.757
b = 16.793

# Input: Latitude
# Output: The expected body mass (kg) of a moose living at the input latitude.
def moose_body_mass(latitude):
    mass = a*latitude + b
    return mass
    
if __name__ == '__main__':
    moose_mass = moose_body_mass(42.922)
    print(moose_mass)