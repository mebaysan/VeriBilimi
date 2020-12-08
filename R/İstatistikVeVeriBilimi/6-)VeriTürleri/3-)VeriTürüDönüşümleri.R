x <- c(12,13,14,15,16) # R default olarak numeric atar

xi <- as.integer(x) # x vektörünü integer'a çevir
class(xi)
is.integer(xi)



y <- c('A','B','C','D','E')
class(y)

yf <- as.factor(y) # ordinal (faktör) türe çevirdi
class(yf)


xc <- as.character(x) # vektörün elemanlarını karaktere çevirir
class(xc)
is.character(xc)

z <- c(0,1,1,0,1,1,0,1,1)
zl <- as.logical(z) # 0 ve 1'i TRUE FALSE'a çevirir
class(zl)

as.logical(c(0,1,11,12)) # 0 olan değerler FALSE olurken 1 ve büyük değerler TRUE olur


as.logical(c('A','B','C')) # karakterleri logical olarak çevirmek istersek NA alırız

