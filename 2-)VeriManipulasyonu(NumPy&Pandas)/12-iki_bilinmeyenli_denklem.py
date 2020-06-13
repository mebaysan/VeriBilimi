#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:18:27 2020

@author: baysan
"""


"""
DENKLEM

5 * x0 + x1 = 12

x0 + 3 * x1 = 10

"""

import numpy as np

a = np.array([[5,1],[1,3]])
b = np.array([12,10])

cevap = np.linalg.solve(a,b)

print(cevap)