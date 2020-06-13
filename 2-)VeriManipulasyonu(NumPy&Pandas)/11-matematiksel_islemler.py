#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:45:08 2020

@author: baysan
"""


import numpy as np

nd = np.arange(1,10)

print(nd*2) # tüm elemanları 2 ile çarptık
# Tabi bunun diğer matematiksel operatörler ile kullanmak da mümkündür

 
print(nd - 1) # tüm elemanlardan 1 çıkarttık

# ufunc

"""
aslında yukarıdaki örnekleri yaptığımızda da numpy arrayleri içerisinde 
otomatik olarak ufunc fonksiyonları çalışmaktadır
"""

print(np.subtract(nd,1)) # nd arrayindeki her bir elemandan 1 çıkarır

print(np.log(nd))

