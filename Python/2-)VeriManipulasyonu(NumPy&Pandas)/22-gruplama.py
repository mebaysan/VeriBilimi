#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:13:18 2020

@author: baysan
"""


# Genellikle gruplama ve toplulaştırma işlemleri bir arada kullanılır

import pandas as pd

df = pd.DataFrame({'gruplar':['A','B','C','A','B','C'],
                   'veri':[10,11,52,23,42,55]},
                    columns = ['gruplar','veri'])

print(df)


print(df.groupby('gruplar').mean()) # yakaladığımız grupların ortalamasını aldık 

