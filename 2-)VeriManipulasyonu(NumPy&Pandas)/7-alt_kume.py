#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 02:56:24 2020

@author: baysan
"""

import numpy as np

# Array Alt Küme İşlemleri (Slicing)

arr = np.random.randint(0,10,10)
"""
# Vektör (Tek boyutlu slice)
print(arr[0:3]) # 0. index ile 3. index arasını al
print(arr[:3]) # 0. index ile 3. index arasını al
print(arr[3:]) # 3. indexten sonrasını al
print(arr[1::2]) # 1. indexten son indexe kadar git 2'er 2'er atla
print(arr[-1]) # son indexi verir
"""



# Matris (Çok boyutlu slice)

nd = np.random.randint(0,10,(5,5))
print(nd[:,0]) # bütün satırları seç ve sadece 0. sütunları al

print(nd[0,:]) # 0. satır ve tüm sütunlar

print(nd[0:2,0:3]) # 0 ile 2'e kadar satırlar, 0 ile 3 arası sütunlar

print(nd[0:,0:2])