x <- c(12,56,78,1,4,97,56,34,21,11,192,32,534)

sort(x) # default olarak verileri küçükten büyüğe sıralar

sort(x,decreasing = TRUE) # decreasing = T -> verileri büyükten küçüğe sıralar


y <- c('Enes','ENes','Baysan','Yavuz','Yusuf','YaVuz')

sort(y) # karakter vektörlerini küçükten büyüğe sıraladı

sort(y,decreasing = T) # karakter vektörünü büyükten küçüğe sıraladı


na <- c(NA,x,NA)
na
sort(na) # NA değerleri sıralamaya sokmadı

sort(na,na.last = NA) # NA değerlerini sıralamaya sokmaz
sort(na,na.last = T) # bütün değerleri sıralar en son olarak NA değerleri ekler 
sort(na,na.last = F) # bütün değerleri sıralar ilk olarak NA değerleri ekler 


indisli <- sort(na,decreasing = T,na.last=T,index.return=T) # bize 2 vektör döner. x -> sıralanmış değerler vektörü, ix -> sıralanmış vektörlere ait indis vektörü. bize liste döner
class(indisli)
indisli[['x']] # sıralanmış değerlere ait vektör
indisli[['ix']] # sıralanmış değerlerin indislerine ait vektör
en_buyuk = indisli[['ix']][1] # en büyük değere ait indis
na[en_buyuk] # vektörden en büyük değere ait olan indis ile en büyük değere ulaşırız
