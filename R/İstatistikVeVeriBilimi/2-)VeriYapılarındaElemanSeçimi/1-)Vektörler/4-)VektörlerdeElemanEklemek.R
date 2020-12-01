x <- seq(11, 66, by = 11) # 11'den 66'a kadar bir vektör oluştur, her seferinde 11 artsın
x
length(x)

x[length(x)+1] = 77 # x'in (mevcut eleman sayısı + 1). elemanı 77 olarak set et
x


y <- c(1:10)
y

y[c(11:20)] = c(20:29) # y'nin 11 ile 20 (dahil) arasındaki elemanlarına sırasıyla 20 ile 29 arasındaki elemanları ekle
y

z <- c(1:5)
z

z[6:10] = 100 # z'nin 6 ile 10 (dahil) a kadar elemanlarını 100 yap
z

z[13] = 1000 # z'nin 13. elemanını 1000 yap. 11 ve 12 elemanları daha önce olmadığından NA olarak set edecek
z
