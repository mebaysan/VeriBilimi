#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:03:12 2020

@author: baysan
"""


import pandas as pd
import numpy as np


s1  = np.random.randint(0,10,5)
s2  = np.random.randint(0,10,5)
s3  = np.random.randint(0,10,5)

sozluk = {'var1':s1,'var2':s2,'var3':s3}

df = pd.DataFrame(sozluk) # sözlük üzerinden DataFrame oluşturduk

print(df)


print(df[0:1]) # 0'dan 1'e KADAR (yani 0. index) olan değerler

print(df.index) # index hakkında bilgi sahibi oluruz

df.index = ['a','b','c','d','e'] # index değerlerini değiştirdik

print(df)


# silme işlemi
df.drop('a',axis=0,inplace=True) # inplace argümanı DataFrame üzerinde yapılan değişikliğin kalıcı olmasını sağlar
            # axis = 0 -> satır, axis = 1 -> sütun
print(df)


# fancy ile silme
silinecekler = ['c','e']
print(df.drop(silinecekler,axis=0)) # yukarıdaki gibi inplace argümanını kullanmazsak yapmış olduğumuz değişiklik kalıcı olmayacaktır

print('var1' in df) # 'var1' adında bir değişken df içerisinde var mı


df['var4'] = [1,2,3,4] # DataFrame içerisinde var4 adında bir değişken oluşturduk
print(df)

df['var4'] = df['var1'] / df['var2'] # var4 değişkeninin değerlerini var1 ve var2 değişkenlerinin bölümünden oluşturduk
print(df)


# değişken silmek
df.drop('var4',axis=1,inplace=True) # 1 sütunları temsil ettiğinden argümanı 1 olarak yolluyoruz ve inplace argümanı yapılan değişikliğin kalıcı olmasını sağlıyor
print(df)

