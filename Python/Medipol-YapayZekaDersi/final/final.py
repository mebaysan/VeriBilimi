#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:39:58 2021

@author: mebaysan [Muhammed Enes Baysan]
"""
import numpy as np # veri setini okumak ve manipüle etmek için
import pandas as pd # veri setini okumak ve manipüle etmek için
from sklearn.model_selection import train_test_split # veri setini test ve eğitim olarak ayırmak için
from sklearn.tree import DecisionTreeClassifier  # ağaç için
from sklearn.metrics import accuracy_score # accuracy'i hesaplamak, modelin doğruluğunu kontrol etmek için kullanacağız
from sklearn.cluster import KMeans # KMeans için kullanacağımız fonksiyon
from sklearn.decomposition import PCA,IncrementalPCA # pca analizi için paketler


def veri_getir(file_name):
    # Soru 1
    data = np.genfromtxt(file_name,delimiter=',',names=True,encoding='utf-8',dtype=None) # veri setini array olarak okuyoruz
    return data


def veri_seti_getir(data):
    df = pd.DataFrame(data) # okuduğumuz array'i dataframe haline geitiriyoruz
    return df


def normalize_et(df,col_name,min,max,new_col_name):    
    # Soru 3
    yeniCol = df[col_name]
    # Soru 4
    df.drop(col_name,axis=1,inplace=True) # normalize_TSH kolonunu df'den kaldırıyoruz
    df.insert(value=yeniCol,column=new_col_name,loc=0) # 0. colon indisine yeni kolonumuzu ekliyoruz
    return df

def verileri_bol(df,test_size):
    # Soru 5
    X = df.iloc[:, 0:3] # feature değişkenimiz hariç diğer değişkenleri seçiyoruz
    y = df.iloc[:,-1:] # feature (tahmin etmek istediğimiz) değişkeni seçiyoruz
    X_train, X_test, y_train, y_test = train_test_split(X,  # hangi değerler ile tahmin edeceğiz
                                                    y, #  hangi sınıfları tahmin edeceğiz (hedef feature)
                                                    test_size=test_size,  # test büyüklüğü %30 olacak
                                                    random_state=100  # random olarak makinaya bırakıyoruz
                                                   )
    return X_train, X_test, y_train, y_test



def gini_sinifla_hesapla(X_train,y_train,test_list):
    # Soru 6
    clf_gini = DecisionTreeClassifier(
        criterion='gini',  # hangi kritere göre classifier edelim (gini || entropy)
        random_state=100,
        max_depth=3,  # max derinlik 3 olsun, ağacın max derinliği 3 olacak
        min_samples_leaf=5  # yaprakta min bulunacak eleman sayısı 5 olacak
    )
    clf_gini.fit(X_train, y_train) # modeli eğitiyoruz
    print(f"gini ile gelen sınıfın tahmini = {clf_gini.predict([test_list])}") # bu değerlerde gelen bir örnek varsa bunun sınıfı nedir (gini tahmin)
    return clf_gini


def entropy_sinifla_hesapla(X_train,y_train,test_list):
    # Soru 6
    clf_entropy = DecisionTreeClassifier(
    criterion='entropy',  # hangi kritere göre (gini || entropy)
    random_state=100,
    max_depth=3,
    min_samples_leaf=5
    )
    clf_entropy.fit(X_train, y_train)
    print(f"entropy ile gelen sınıfın tahmini = {clf_entropy.predict([[5, 2, 3]])}") # bu değerlerde gelen bir örnek varsa bunun sınıfı nedir (entropy tahmin)
    return clf_entropy


def gini_acc(gini,X_test,y_test):
    # Soru 7
    y_pred_gini = gini.predict(X_test) # oluşturduğumuz classifier ile X_test verilerini tahmin ediyoruz (gini)
    print("gini accuracy = {}".format(accuracy_score(y_test, y_pred_gini)))  # yaptığımız tahmini karşılaştırıyoruz
    return y_pred_gini



def entropy_acc(entropy,X_test,y_test):
    # Soru 7
    y_pred_ent = entropy.predict(X_test) # oluşturduğumuz classifier ile X_test verilerini tahmin ediyoruz(entropy)
    print("entropy accuracy = {}".format(accuracy_score(y_test, y_pred_ent)))
    return y_pred_ent


def kmeans_kumele(k,X_train):
    # Soru 8
    kmeans = KMeans(n_clusters=k)  # kaç kümeye ayıracağımızı veriyoruz
    kmeans.fit(X_train)  # modeli parçaladığımız verinin %70'lik kısmı ile eğitiyoruz
    labels = kmeans.labels_  # label'ları alıyoruz
    centroids = kmeans.cluster_centers_  # küme merkezlerini alıyoruz
    return kmeans

def kmeans_kumeleri_yazdir(kmeans,X_test):
    # Soru 9
    prediction = kmeans.predict(X_test) # kmeans algoritmasını eğitiyoruz
    print(f"Parçaladığımız verinin %30'luk kısmının KMeans ile tahmin edilmiş kümeleri:\n{prediction}")
    return prediction


def pca_analizi(df):
    X = np.array(df.iloc[:,:-1]) # feature değişkeni pca analizine sokmayacağımız için onu çıkartıp kalan değişkenleri numpy arrayi yapıyoruz
    pca = PCA(n_components=2) # 2 değişkene indirmek istediğimizi söylüyoruz
    pca.fit(X) # pca modeli eğitiyoruz
    print("PCA Ratio: {}".format(pca.explained_variance_ratio_))
    print("PCA Singular Values: {}".format(pca.singular_values_))
    return pca
    



def main():
    data = veri_getir('DataSet_2.csv')
    df = veri_seti_getir(data)
    df = normalize_et(df, 'normalize_TSH', 10, 40, 'Normalize')
    X_train, X_test, y_train, y_test = verileri_bol(df, 0.3)
    clf_gini = gini_sinifla_hesapla(X_train, y_train, [5, 2, 3])
    clf_entropy = entropy_sinifla_hesapla(X_train, y_train, [5,2,3])
    gini_acc(clf_gini, X_test, y_test)
    entropy_acc(clf_entropy, X_test, y_test)
    kmeans = kmeans_kumele(4, X_train)
    kmeans_kumeleri_yazdir(kmeans, X_test)
    pca_analizi(df)
    

main()









