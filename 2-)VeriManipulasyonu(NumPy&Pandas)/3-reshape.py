#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:16:41 2020

@author: baysan
"""


import numpy as np

nd = np.arange(1,10)

"""
oluşturduğumuz bu ndarray üzerinden yeni bir 3x3'lük bir nd array oluşturmak 
istersek reshape fonksiyonunu kullanmamız gerekmektedir.
Fonksiyonların çıktısı matris veya vektör olduğundan biz de bunları tekrar istediğimiz
şekilde boyutlandırabiliriz. Bu işleme reshape denmektedir.
"""

rs = nd.reshape(3,3)

print(rs)


"""
Bazı durumlarda bazı fonksiyonlar tek boyutlu arrayleri kabul etmemektedir.
Bu tür durumlarda tek boyutlu arrayimizi (vektör) vektör halindeki yapısını bozmadan
matris haline getirebiliriz. Bunun için de reshape fonksiyonunu kullanabiliriz.

"""

arr = np.arange(1,10)
print(arr)
arr_degisen = arr.reshape((1,9))
print(arr_degisen)
print(arr_degisen.ndim)