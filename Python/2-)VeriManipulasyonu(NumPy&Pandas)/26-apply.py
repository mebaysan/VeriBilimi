#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:06:43 2020

@author: baysan
"""


import pandas as pd


df = pd.DataFrame({
                   'degisken1':[10,23,33,22,11,99],
                   'degisken2':[100,253,333,262,111,969]},
                  columns = ['degisken1','degisken2'])

"""
apply -> DataFrame'in değişkenlerinin üzerinde gezinme yeteneği olan ve aggregation
(toplulaştırma) işlemleri yapmamızı sağlayan bir fonksiyondur.
"""


def custom_sum(sutun):
    toplam = 0
    for gozlem in sutun:
        toplam += gozlem
    return toplam

print(df.apply(custom_sum)) # her değişken üzerinde istediğimiz fonksiyonları çalıştırabiliriz

