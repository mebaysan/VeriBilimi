#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:54:02 2020

@author: baysan
"""

import pandas as pd

df = pd.DataFrame({'gruplar':['A','B','C','A','B','C'],
                   'degisken1':[10,23,33,22,11,99],
                   'degisken2':[100,253,333,262,111,969]},
                  columns = ['gruplar','degisken1','degisken2'])


# kendi tanımladığımız fonksiyonu değişkenlere uygulayabiliriz

df = df.iloc[:,1:]

print(df.transform(lambda x: x-x.mean()))
# her veriyi kendisi - kendisinin ortalaması ile eşitledik
"""
transform fonksiyonunu belirlediğimiz bir fonksiyona dönüştürmek üzere kullanabiliriz
"""

# transform vektörel çalışan bir fonksiyondur.