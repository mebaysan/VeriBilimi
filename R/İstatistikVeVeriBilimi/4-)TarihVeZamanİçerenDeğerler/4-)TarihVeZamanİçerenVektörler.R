
d <- c('23/06/2000','10/10/1979','14/08/2010')

dv <- as.Date(d,format='%d/%m/%Y') # vektörün tüm elemanlarını Date tipine çeviriyoruz

dvr <- rep(dv,times=5,each=3) # her değer kendi içinde 3 kere tekrar etsin ve bu işlem 5 kere tekrar etsin
length(dvr)


t <- rep(Sys.time(),times=5,each=3)

tp <- as.POSIXlt(t)

tp$year+1900 # vektörün tüm elemanlarına 1900 ekledik, yani tarihi aldık

tp$sec
