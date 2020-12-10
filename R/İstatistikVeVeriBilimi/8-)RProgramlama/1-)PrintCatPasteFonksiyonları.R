print("Naber")

x <- 5

print(x)

y <- 10

#print(x,y) # yazdırmaz

print(x);print(y);


cat(x,y) # aynı anda farklı şeyleri yazdırmak istersek cat fonksiyonunu kullanırız

cat(x, 'x 2 = ',x*2)

cat('1. satır','\n','2. satır')


text <- paste(x,'x 2 = ',x*2) # paste fonksiyonu oluşturduğu stringi değişkene atamamızı sağlar (character vektörü olarak)


paste('Arada','boşluk','var') # aralarına otomatik olarak boşluk koyar
paste0('Arada','boşluk','yok') # aralarına boşluk koymaz (eğer biz koymadıysak)
# paste fonksiyonu string oluşturur