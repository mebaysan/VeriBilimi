#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 20:28:29 2020

@author: baysan
"""


import numpy as np

# Vektör
arr = np.array([3,1,2,6,74,6,8,9,12])
print(np.sort(arr))
print(arr)


# Matris
arr = np.random.normal(20,5,(3,3))
print(np.sort(arr,axis=0))