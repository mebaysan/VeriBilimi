#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:12:57 2020

@author: baysan
"""


import pandas as pd
import numpy as np

# Gözlem ve Değişken Seçimi: loc & iloc

nd = np.random.randint(1,30,(10,3))
df = pd.DataFrame(nd,columns=['var1','var2','var3'])

print(df)

# loc -> tanımlandığı şekliyle seçim yapmak için kullanılır
print(df.loc[0:3]) # 3. indexte dahil


# iloc -> alışık olduğumuz indexleme mantığı ile seçim yapar
print(df.iloc[0:3]) # 3. index dahil değil



# hem satır hem sütun olarak seçmek
print(df.iloc[:3,:2]) # 3. satıra kadar 2. sütuna kadar


print(df.loc[0:3,'var3']) # eğer değişken ya da gözlemlerle ilgili kesin bir işaretleme yapacaksak 'loc' kullanmalıyız

# print(df.iloc[0:3,'var3']) # hata verecektir


print(df.iloc[0:3]['var3']) # 3. satıra KADAR 'var3' değişkeni

