#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:58:49 2020

@author: baysan
"""


import numpy as np 

"""
- ndim -> boyut sayısı
- shape -> boyut bilgisi
- size -> toplam eleman sayısı
- dtype -> array veri tipi

"""


nd = np.random.randint(0,10,10)
print(nd)
print(nd.ndim)
print(nd.shape)
print(nd.size)
print(nd.dtype)