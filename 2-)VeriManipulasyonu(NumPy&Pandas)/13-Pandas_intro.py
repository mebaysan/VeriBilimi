#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:27:27 2020

@author: baysan
"""


import pandas as pd


df = pd.Series([11,22,33,44,55,66,77,88,99]) # Pandas seri oluşturmak

# Pandas serileri değerleri index numaraları ile beraber yapar

print(df)

print(type(df)) # veri tipini öğrenmek


print(df.axes) # serinin index bilgilerine erişebiliriz

print(df.dtype) # serinin tipini öğreniriz

print(df.size) # serinin eleman sayısını verir

print(df.ndim) # serinin boyutunu verir

print(df.values) # array formunda sadece verilere (değerlere) erişebiliriz

print(df.head(5)) # serinin ilk 5 değerini getirir

print(df.tail(5)) # serinin son 5 elemanını getirir

# index isimlendirme
df = pd.Series([12,23,34,45,56],index=['x','y','z','w','q']) # indexleri istediğimiz şekilde isimlendirebiliriz
print(df)

print(df['x']) # isimlendirdiğimiz index'e karşılık gelen değer

print(df['x':'z']) # x index'inden z index'ine kadar slice

# sözlük üzerinden seri oluşturmak
df = pd.Series({'reg':10,'log':11,'cat':12})
print(df)
print(df['reg':'log']) # slice

# iki seriyi birleştirerek yeni bir seri oluşturmak
seri1 = pd.Series([1,2,3],index=['x1','y1','z1'])
seri2 = pd.Series([4,5,6],index=['x2','y2','z2'])
df = pd.concat([seri1,seri2]) # unutmamalıyız yalnızca 2 seri tipini birleştirir
print(df)
