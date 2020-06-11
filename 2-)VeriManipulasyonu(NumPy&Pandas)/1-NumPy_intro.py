#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:27:43 2020

@author: baysan
"""

import numpy as np  # kütüphaneyi dahil ettik

# ndarray Oluşturmak
nd_array = np.array([1,2,3]) # ndarray oluşturduk
print(type(nd_array)) # oluşturduğumuz nd_array değişkeninin tipi



# İstediğimiz tipte ndarray oluşturmak
nd_array = np.array([1.56,4,5,6],dtype="int") # belirttiğimiz tipte ndarray
print(nd_array)



# Sıfırlardan (0) oluşan ndarray
nd_array = np.zeros(10,dtype='int')
print(nd_array)



# Birlerden (1) oluşan ndarray
nd_array = np.ones((3,4),dtype='int')
print(nd_array)



# İstediğimiz 2 sayı arasında n adet sayıdan oluşan ndarray
nd_array = np.full((2,5),5)
print(nd_array)



# Doğrusal Diziler
nd_array = np.arange(0,28,7)
print(nd_array)



# 2 sayı arasında n adet sayıdan oluşan ndarray
nd_array=np.linspace(0,5,4)
print(nd_array)



# Dağılımını kendimiz belirttiğimiz ndarray
nd_array = np.random.normal(5,8,(4,4)) # ilk parametre ortalama, ikinci parametre standart sapma, 3. parametre ndarray vektör mü matris mi?
print(nd_array)



# Rastgele değerlerden oluşan ndarray
nd_array = np.random.randint(5,20,(3,4)) # 5 ile 20 arasında sayılardan oluşan 3 satır 4 sütündan oluşan ndarray 
print(nd_array)