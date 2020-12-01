x <- list(11,12,c('A','B','C'))
x
"
[]   -> liste olarak döner
[[]] -> vektör olarak döner
"
x[1] # x listesinin 1. elemanı (list olarak döner)
class(x[1]) # class fonksiyonu sayesinde parametre olarak gelen değişkenin tipini öğrenebiliriz

x[[1]] # x listesinin 1. elamanını vektör olarak al
class(x[[1]])


x[[3]] # 3. elemanı vektör olarak döner
x[[3]][2] # 3. elemanın (vektör) içerisindeki 2. elemanı (string) al


y <- list('A' = c(1:4), 'B' = seq(11,44,by=11))
y
names(y) # names fonksiyonu bize listenin içerisindeki isimleri (indis) verir

class(y['A'])
class(y[['A']])

y$A # liste içerisindeki indisleri seçebiliriz
class(y$A)
