#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 11:44:05 2020

@author: baysan
"""


import numpy as np

nd = np.random.randint(0,10,(5,5))

alt_nd = nd[0:3,0:2] # 0. index'ten 3. index'E KADAR satırlar, 0. index'ten 2. index'e kadar sütunlar

alt_nd[0,0] = 1234 # bu durumda alt_nd matrisinin 0. satır 0. sütundaki değerini değiştirdik ama bunu nd değişkeninden aldığımız için nd değişkeninin de 0. satır 0. sütunu değişti
alt_nd[1,1] = 56789

print(nd)

"""
Yukarıdaki gibi alt küme üzerinde işlem yaptığımızda ana kümemizin etkilenmesini 
istemiyorsak 'copy' fonksiyonunu kullanırız
"""
nd = np.random.randint(0,10,(5,5))

alt_kume = nd[0:3,0:2].copy()
alt_kume[0,0] = 9999
print(alt_kume)
print(nd)