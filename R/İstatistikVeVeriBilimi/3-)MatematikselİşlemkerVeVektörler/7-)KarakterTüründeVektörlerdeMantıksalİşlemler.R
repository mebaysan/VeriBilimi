# which fonksiyonu bize indisleri verir

x <- c('A','B','C','D','E','A','B','C')

x[x=='B'] # x'in 'B'ye eşit olan elemanları

x[x < 'C'] # alfabetik sıraya göre 


which(x > 'D') # D'den büyük olan elemanların indislerini verir

x[which(x > 'D')]
