# listede bir eleman sileceksek onu NULL olarak set etmemiz gerekir


x <- list(1,2,3,c(11,22,33))
x



x[[1]] = NULL # listenin 1. elemanını seç (liste olarak)
x


x[[3]] = x[[3]][-3] # x listesi içerisindeki 3. elemanın (vektör) 3. indisini çıkartıyoruz

x


y <- list('A' = c(1:10), 'B' = seq(1,10,by=2),'C'=c('A','B','C','D'))
y

y[['A']][length(y[['A']])] = y[['A']][length(y[['A']])] * y[['A']][length(y[['A']])]

y[['C']] = NULL # y'nin C indisini sil

y$B = seq(9,1,by=-2) # y'nin B indisini 9'dan 1'e kadar 2'er 2'er azaltarak guncelle

y[-2] # y'nin 2. elemanını siler fakat bunun için atama yapmamız gerekir
