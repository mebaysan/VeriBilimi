
d1 <- '23/06/2000'
d2 <- '18/09/2003'

d1 <- as.Date(d1,format='%d/%m/%Y')
d2 <- as.Date(d2,format='%d/%m/%Y')

d1 - d2 # 2 tarih arasındaki fark
class(d1 - d2) # 2 tarih arasındaki farkın sınıfı

as.double(d1 - d2) # 2 tarih arasındaki farkın gününü alıyoruz direkt


t1 <- as.POSIXlt(Sys.time())
t2 <- as.POSIXlt('2020-12-01 00:00:00', format='%Y-%m-%d %H:%M:%S')

t1 - t2 # gün olarak farkı verir

as.double(t1 - t2)
as.integer(t1 - t2)
