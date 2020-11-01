#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:18:39 2020

@author: baysan
"""


"""
Sık kullanılan toplulaştırma (aggregation)
count  -> değişken içerisinde kaç adet değer var
mean   -> değişkene ait verilerin ortalaması
median -> değişkene ait verilerin medyanı
min    -> değişken içerisindeki minimum değer
max    -> değişken içerisindeki maximum değer
std    -> değişkenin standart sapması
var    -> değişkenin varyansı
sum    -> değişkene ait değerlerin toplamı
"""
import seaborn as sns

df = sns.load_dataset('planets')
print(df.count())

print(df.min())

print(df.describe().T) # DataFrame'in betimsel istatistiklerini alabiliriz

print(df.dropna().describe().T) # DataFrame'deki eksik gözlemleri yoksayarak betimsel istatistikleri verir
