#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:05:38 2020

@author: baysan
"""


import numpy as np
import pandas as pd

nd = np.random.randint(1,30,(5,3))
df = pd.DataFrame(nd,columns=['var1','var2','var3'])

print(df)


df2 = df + 99 # df DataFrame'inin her gözlemine 99 ekleyerek yeni bir DataFrame oluşturduk

yeni_df = pd.concat([df,df2])
print(yeni_df)




yeni_df = pd.concat([df,df2],ignore_index=True) # index'leri sıfırdan numaralandırmak için kullanılır
print(yeni_df)



# değişken isimleri farklı olan DataFrame'leri değiştirmek

df2.columns = ['var1','var2','deg3'] # df2 DataFrame'inin değişken isimlerini (kolon/sütun) değiştiriyoruz

print(df.columns)
print(df2.columns)

print(pd.concat([df,df2])) # bize uyarı verecektir, çünkü df ve df2'nin değişken isimleri aynı değildir

print(pd.concat([df,df2],join='inner',ignore_index=True)) # yukarıdaki gibi bir senaryoda 'join' argümanını veririz ve 2 dataframe'in de sadece kesişen (aynı) değişkenlerini birleştirir

