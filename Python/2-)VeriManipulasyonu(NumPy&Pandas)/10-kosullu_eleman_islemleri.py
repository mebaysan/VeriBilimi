#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:35:13 2020

@author: baysan
"""


import numpy as np

nd = np.arange(0,10)

print( nd < 4) # nd arrayi içerisindeki elemanlar 3 değerinden küçük mü?

# Fancy ile yakalama

dortten_kucukler = nd[nd < 4]

print(dortten_kucukler)
