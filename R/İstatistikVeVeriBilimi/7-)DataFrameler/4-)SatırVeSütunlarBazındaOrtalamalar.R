data()


View(iris)

rowMeans(iris[,c(1:ncol(iris) -1)]) # tüm satırların ortalamasını alır, parametre olarak gelen tüm değişkenler numerik olmalıdır!

ort <- rowMeans(iris[,c(1:ncol(iris) -1)])

iris['Ortalama'] <- ort # iris veri setine yeni bir değişken atadık
View(iris)



colMeans(iris[1:ncol(iris)-1])

data(iris)
colMeans(iris[1:ncol(iris)-1]) # sütunların ortalamasını verir, değişkenler numerik olmalıdır




colMeans(iris[1:ncol(iris)-1],na.rm=T) # NA değerleri dahil etmememiz gerekir

