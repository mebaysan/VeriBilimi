#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:25:44 2020

@author: baysan
"""


# Pandas DataFrame Oluşturmak

import pandas as pd
import numpy as np

df = pd.DataFrame([1,2,45,67,879,90],columns=["degisken_adi"]) # ilk argüman hangi veriyi DataFrame'de kullanacağımız ve 2. argüman ise kolon adı (opsiyonel)

print(df)

nd = np.arange(1,10).reshape((3,3))
df = pd.DataFrame(nd,columns=['var1','var2','var3'])
print(df)


print(df.columns) # değişken isimlerini getirir

df.columns = ('deg1','deg2','deg3') # değişken isimlerini değiştirebiliyoruz
print(df)

print(df.axes) # satır ve sütun bilgilerini verir

print(df.ndim) # boyut sayısını verir

print(df.shape) # kaça kaçlık

print(df.size) # kaç elemanlı

print(df.values) # sadece değerleri verir ve ndarray nesnesine çevirir

print(df.head(2)) # baştan 2 veri

print(df.tail(2)) # sondan 2 veri