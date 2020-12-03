# length fonksiyonu sayesinde vektörlerin eleman sayısını bulabiliriz

x <- c(1:1000)
length(x)

x <- seq(1,100000,by=3) # 1'den 100.000'e kadar 3'er 3'er bir vektör oluştur
length(x)


x[length(x)] # sonuncu indis

x[length(x)-1] # sondan bir önceki indis

x[length(x) + 1] = 1 # vektöre bir eleman ekle

x[length(x)]
