#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:36:45 2020

@author: baysan
"""


import pandas as pd

df = pd.DataFrame({'gruplar':['A','B','C','A','B','C'],
                   'degisken1':[10,23,33,22,11,99],
                   'degisken2':[100,253,333,262,111,969]},
                  columns = ['gruplar','degisken1','degisken2'])


print(df)

"""
kendi yazdığımız özel fonksiyonları DataFrame'lerdeki değişkenlere gönderip
filtre işlemi yapmamızı sağlayan işlemin adı 'filter'dır.

"""


def custom_filter(x):
    return x['degisken1'].std() > 9


print(df.groupby('gruplar').filter(custom_filter))

# degisken1'e göre standart sapmalar hesaplandı ve 9'dan büyük olanlar geldi
