#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:24:36 2020

@author: baysan
"""


import pandas as pd
import numpy as np

df = pd.DataFrame({'gruplar':['A','B','C','A','B','C'],
                   'degisken1':[10,23,33,22,11,99],
                   'degisken2':[100,253,333,262,111,969]},
                  columns = ['gruplar','degisken1','degisken2'])


print(df)


print(df.groupby('gruplar').mean())


print(df.groupby('gruplar').aggregate(['min',np.median,'max']))

"""
pandas'ın içerisinde olduğunu bildiğimiz fonksiyonları çalıştırmak istersek
bunları ' ' içerisinde yazmamız gerekmektedir.
"""