# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:22:30 2021

@author: Nate
"""

# Constants
c = 299792458

# Input: A distance in meters (m).
# Output: The time it takes for light to travel the input distance, in seconds (s).
def light_time(distance):
    return distance/c
    
    
if __name__ == '__main__':
    prox_centauri_dist = 4.01419E16 # distance in m 
    prox_centauri_lightime = light_time(prox_centauri_dist)
    print(prox_centauri_lightime)
    
    moon_dist = 384400*1000 # distance in m
    moon_lightime = light_time(moon_dist)
    print(moon_lightime)
    
    