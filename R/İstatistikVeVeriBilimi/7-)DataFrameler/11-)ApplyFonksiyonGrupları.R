View(iris)

apply(
  iris[,c(1:ncol(iris)-1)], # hangi veri seti
  MARGIN=1, # 1 -> satırlar, 2 -> sütunlar bazında fonksiyonu uygular
  FUN = mean # hangi fonksiyonu uygulayacak
  ) # tüm satırlardaki numeric değişkenlerin ortalamasını alır


apply(
  iris[1:4],
  MARGIN=2, # sütunların ortalamasını alır
  FUN=mean
)


apply(iris[1:4],MARGIN = 2,FUN=sum) # tüm sütunların toplamını alır


lapply(iris[1:4], FUN=sum) # lapply fonksiyonu ise listeler üzerinde kullanılır, df üzerinde kullanırsak direkt olarak sütunlar(değişkenler) üzerinde fonksiyonları çalıştırır



mylist <- list('a'=c(1,2,3,4),'b'=c(5,6,7,8),'c'=c(9,10,11,12))
lapply(mylist,FUN=sum) # listemiz üzerinde fonksiyonu uygulayabiliriz

