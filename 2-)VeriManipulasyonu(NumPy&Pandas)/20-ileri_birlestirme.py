#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 16:30:07 2020

@author: baysan
"""


import pandas as pd

df1 = pd.DataFrame({'calisanlar':['Ali','Veli','Ayse','Fatma'],
                    'grup':['Muhasebe','Muhendislik','Muhendislik','İK']})
# print(df1)

df2 = pd.DataFrame({'calisanlar':['Ayse','Ali','Veli','Fatma'],
                    'ilk_giris':[2010,2009,2014,2019]})
# print(df2)



"""
                        bire bir birleştirme işlemi
 Tüm elemanların 2 verisetinde de yer almasıdır. Bu örnek için 2 verisetinde de
calisanlar bulunmaktadır.
"""
#print(pd.merge(df1,df2)) # merge hangi değişkene göre birleştireceğini otomatk bulmaktadır

print(pd.merge(df1,df2,on='calisanlar')) # istersek 'on' parametresi ile hangi değişkene göre birleştireceğini söyleyebiliriz



"""
                        çoka bir birleştirme
2 verisetinde de olan 'grup' değişkenine göre birleştirme işlemi gerçekleştirildi
"""

df3 = pd.merge(df1,df2)

df4 = pd.DataFrame({'grup':['Muhasebe','Muhendislik','İK'],
                    'mudur':['Caner','Mustafa','Berkcan']})

print(pd.merge(df3,df4))


"""
                        çoka çok birleştirme
2 verisetinde de olan 'grup' değişkenine göre birleştirme işlemi gerçekleştirildi

"""

df5 = pd.DataFrame({'grup':['Muhasebe','Muhasebe','Muhendislik','Muhendislik','İK','İK'],
                    'yetenekler':['matematik','excel','kodlama','linux','excel','yonetim']})


print(pd.merge(df1,df5))