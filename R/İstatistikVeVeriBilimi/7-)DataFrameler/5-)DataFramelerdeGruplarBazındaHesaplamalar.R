View(iris)

aggregate(iris[,1:ncol(iris)-1], by = list(iris$Species), FUN = mean)
# aggregate fonksiyonu sayesinde istediğimiz bir fonksiyonu seçtiğimiz verisetine uygulayabiliriz
# by parametresi liste alır, hangi değişkene göre gruplayacağımız
# FUN hangi fonksiyonu kullanmak istediğimiz (sd, mean, sum)



aggregate(iris[,1:ncol(iris)-1], by = list(iris$Species), FUN = mean,na.rm=T)
# na.rm = T -> NA değerleri hesaba katma
