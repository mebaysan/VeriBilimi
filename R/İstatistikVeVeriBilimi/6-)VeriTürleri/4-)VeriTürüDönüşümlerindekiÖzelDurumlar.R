x <- factor(c('A','B','C','D'))
class(x)

as.numeric(x) # faktörü numeriğe çevirirken alfabetik sıraya göre 1'den başlayıp değer atamaya başlar

as.numeric(factor(c('B','A','C','D','A','C')))



cf <- factor(c('D','A','C','B'),levels=c('B','C','A','D')) # levels parametresi ile ordinal değişkenin seviyelerini kendimiz belirliyoruz
cf




nf <- factor(c('10','13','24','34','65'))
as.numeric(nf) # sayısal karakterli faktörleri numeric vektörlere çevirmek istersek önce karaktere sonra numeric vektöre çevirmeliyiz
as.numeric(as.character(nf))

