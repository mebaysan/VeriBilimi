#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:52:45 2020

@author: baysan
"""


import numpy as np

# Vektör ayırmak 

x = np.array([1,2,3,99,99,3,2,1])

spl = np.split(x,[3,5])
print(spl)


# Bu örnek bildiğimiz gibi bize 3 adet ndarray return ediyor. Bu return edilen ndarrayleri sırasıyla a b c değişkenlerine atadık
a,b,c = np.split(x,[3,5])
print(a,b,c)

print("**********************************\n")


# Matris ayırma

## Dikey olarak bölmek
arr = np.arange(0,16,1).reshape([4,4]) # 4x4'lük bir matrisimiz oldu
# 2. satırdan sonraki kısmı bölüp dikey olarak yana ekliyoruz
print(np.vsplit(arr,[2])) # ilk parametre hangi ndarray bölünecek, 2. parametre hangi elemana kadar bölünecek

ust,alt = np.vsplit(arr,[2])

print(ust)
print(alt)

## Yatay olarak bölmek
arr = np.arange(0,16,1).reshape([4,4])
print(np.hsplit(arr,[2]))