#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:39:07 2020

@author: baysan
"""


import numpy as np
import pandas as pd

nd = np.random.randint(1,30,(10,3))
df = pd.DataFrame(nd,columns=['var1','var2','var3'])

print(df[df.var1 > 15]) # var1 değişkenindeki değerlerden 15'ten büyük olanlar


print(df[df.var1 > 15]['var1']) # gelen değerlerden var1 değişkeni seçilmiştir


print(df[(df.var1 > 15) & (df.var3 < 5)])