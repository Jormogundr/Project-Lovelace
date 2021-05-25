# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:43:46 2021

@author: Nate

Input: (Latitude, longitude) coordinates of two points. Latitudes go from -90 to +90. Longitudes go from -180 to +180. Remember to convert your angles from degrees to radians before using the sine and cosine functions!

Output: The distance between the points in kilometers (km).
"""

import numpy as np

# Consts
R = 6372.1 # radius of earth, km

def haversine_distance(phi1, lamda1, phi2, lamda2):
    # convert degrees to radians
    phi1 = degToRad(phi1)
    phi2 = degToRad(phi2)
    lamda1 = degToRad(lamda1)
    lamda2 = degToRad(lamda2)
    
    prefactor = 2*R
    arg1 = np.sin((phi2 - phi1)/2)**2
    arg2factor = np.cos(phi1)*np.cos(phi2)
    arg2 = arg2factor*np.sin((lamda2 - lamda1)/2)**2
    return prefactor*np.arcsin(np.sqrt(arg1 + arg2))

def degToRad(p):
    p_ = p*(np.pi/180)
    return p_
    
point1 = [46.283, 86.667]
point2 = [-48.877, -123.393]
print(haversine_distance(*point1, *point2))