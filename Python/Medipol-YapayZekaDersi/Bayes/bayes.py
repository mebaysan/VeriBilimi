#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:07:53 2021

@author: gokhansilahtaroglu
"""

from sklearn.model_selection import train_test_split 
# verileri eğitim ve test verisi olarak ayırmak için kullandığımız fonksiyon
from sklearn.naive_bayes import GaussianNB
# Bayes istatistiğini kullanarak verileri değerlendirmek için kullandığımız sınıf
import numpy as np
# verileri okuyup bölmek için kullandığımız sınıf


verilerim = np.loadtxt('iris_training.csv', # veri seti
                       delimiter = ',' # veri seti ne ile ayrılmış
                       )

X = verilerim[:,0:4] # tahmin etmek için kullanacağımız feature'lar. 0'dan başla 4'e kadar olan kolonları al (0,1,2,3)
y = verilerim[:,4] # tahmin etmek istediğimiz hedef feature



X_train, X_test, y_train, y_test = train_test_split(X, # tahmin etmek için kullanacağımız feature'lar
                                                    y, # tahmin etmek istediğimiz feature'lar
                                                    test_size=0.5, # verinin yüzde kaçını test etmek için kullanacağız (kalanı eğitim için kullanılacak)
                                                    random_state=0 # rastgele olarak verileri %50 %50 olarak ayır
                                                    ) # verileri bölmek için kullandığımız fonksiyon, feature'ları ve hedef feature'ları ayrı ayrı böler


gnb = GaussianNB() # sınıfı kullanmak için bir instance oluşturuyoruz

y_pred = gnb.fit(X_train, # eğitim tahmin feature'larını kullan
                 y_train # eğitim hedef feature'larını kullan
                 ).predict([[3.5, 5.4, 6.42, 2.34]]) # gnb ile X_train ve y_train kullanarak öğren ve sonra bu verilere göre predict (tahmin) et
print('pedicted class number is %d'   %y_pred)

# kendi ayırdığı test grubu ile tahmin et
y_pred = gnb.fit(X_train, # ayırdığın tahmin feature'larını kullan 
                 y_train # ayırdığın hedef feature'ları kullan
                 ).predict(X_test) # tahmin etmek için ayırdığın kendi test verilerini kullan ve tahmin et
print("Number of mislabeled points out of a total %d points : %d"% (X_test.shape[0], (y_test != y_pred).sum()))