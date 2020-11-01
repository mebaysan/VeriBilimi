#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:28:53 2020

@author: baysan
"""


import pandas as pd
import numpy as np

nd = np.array([1,2,34,45,677,75])
seri = pd.Series(nd)

print(seri.index) # index bilgilerine ulaşıyoruz

print(seri.keys) # key değerlerine ulaşırız

print(list(seri.items())) # key-value şeklinde tuple olarak bir listeye alırız

print(seri.values) # serinin sadece değerlerine erişiriz

# elemanları sorgulamak

print("x" in seri) # "x" değeri seri'nin içinde mi sorusunu sorduk

# fancy ile eleman seçmek

print(seri[[1,4]]) # index'i 1 ile 4 olan verileri getirdik

print(seri[1:4]) # index'i 1'den 4'e kadar olan verileri getir

