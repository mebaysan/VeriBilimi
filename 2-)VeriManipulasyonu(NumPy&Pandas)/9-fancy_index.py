#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:27:11 2020

@author: baysan
"""


import numpy as np

# Fancy Index

# Tek Boyut (Vektör)
nd = np.arange(0,30,3) # 0-30 arası 3'erli doğrusal vektör

istenilen_indexler = [1,3,5] # 1. 3. 5. indexleri almak istediğimizi seçtik

print(nd[istenilen_indexler])


# Çok Boyut (Matris)

nd = np.arange(0,9).reshape((3,3)) # tek boyutlu arrayi, boyutlu array haline getirdik
# print(nd)

istenilen_satir = np.array([0,1])
istenilen_sutun = np.array([1,2])

print(nd[istenilen_satir,istenilen_sutun])

# Basit Index ve Fancy Index
nd = np.arange(0,9).reshape((3,3))

print(nd[0,[1,2]]) # 0. satırı al (basit) ve 1 ile 2. sütunları al (fancy)

# Slice ve Fancy Index
nd = np.arange(0,9).reshape((3,3))

print(nd[1:,[1,2]]) # 1. satırdan sonraki satırları al (slice) ve 1 ile 2. sütunları al (fancy)
