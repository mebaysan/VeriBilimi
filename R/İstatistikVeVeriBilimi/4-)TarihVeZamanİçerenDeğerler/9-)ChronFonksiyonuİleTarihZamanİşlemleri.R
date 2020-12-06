# install.packages('chron') # paket yüklememizi sağlar

library('chron') # chron paketini import ediyoruz (aktif ediyoruz)

?chron # chron hakkında yardım

date <- '23/06/2000'

d <- chron(dates.=date,format='d/m/y')
class(d) # chron içerisinde kendisine özel veri tipi

t1 <- '10:30:23'
t2 <- '11:30:46'
t <- chron(times. = c(t1,t2), format = 'h:m:s')
t