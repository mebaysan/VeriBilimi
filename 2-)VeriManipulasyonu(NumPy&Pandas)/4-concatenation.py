#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:33:46 2020

@author: baysan
"""


import numpy as np

# Tek Boyutlu Array (Vektör) Birleştirme
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.array([7,8,9])
xyz = np.concatenate([x,y,z])
print(xyz)


# İki Boyutlu Array (Matris) Birleştirme

x = np.zeros((3,4),dtype='int')
y = np.ones((3,4),dtype='int')
xy = np.concatenate([x,y],axis=1)
# axis = 0 veya 1    0 satırları 1 sütunları
print(xy)

# 2 boyutlu arrayleri manuel oluşturmak istersek
a1 = np.array([[1,2,3],
               [4,5,6]])
a2 = np.array([[7,8,9],
               [10,11,12]])
print("************************\nManuel oluşturulmuş ndarrey concate\n",
      np.concatenate([a1,a2],axis=0))