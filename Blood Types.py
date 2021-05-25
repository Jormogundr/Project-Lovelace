# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:02:38 2021

@author: Nate

Input: The person's blood type as a string, and a list of strings with available blood types.

Output: True if the person can be saved, and false otherwise.
"""

import numpy as np

def survive(blood_type, donated_blood):
    
    blood_db = {
    'A+': ['A+', 'A-', 'O+', 'O-'],
    'A-': ['A-', 'O-'],
    'B+': ['B+', 'B-', 'O+', 'O-'],
    'B-': ['B-', 'O-'],
    'AB+': [True],
    'AB-': ['AB-', 'A-', 'B-', 'O-'],
    'O+': ['O+', 'O-'],
    'O-': ['O-']}
    
    valid_types = blood_type[donated_blood]
    if np.any([valid_types, donated_blood]): return True
    else: return False
    


recipient_type = 'B+'
blood_types = ["A-", "B+", "AB+", "O+", "B+", "B-"]

print(survive(blood_db, recipient_type))
