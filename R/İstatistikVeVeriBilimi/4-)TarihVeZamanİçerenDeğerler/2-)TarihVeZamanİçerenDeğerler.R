
Sys.time() # tarih ve zamanı verir

t1 <- Sys.time()
t1
class(t1)

as.POSIXct(Sys.time()) # unix koduna ihtiyacımız olursa 
as.POSIXlt(Sys.time()) # tarih objesine tek tek ihtiyacımız varsa bu fonksiyon

posix <- unclass(as.POSIXct(Sys.time())) # posix türünde zamanı ve tarihi verir

posix_list <- unclass(as.POSIXlt(Sys.time())) # liste olarak posix verir

class(posix_list)

names(posix_list)

posix_list[['year']] + 1900 # posix türünde olduğu için yılı hesaplarken 1900 eklememiz gerek

posix_list[['mon']] + 1 # ayı hesaplarken de 1 eklememiz gerek


birth_date <- '23/06/2000 10:00:00'
bd <- as.POSIXlt(birth_date, format='%d/%m/%Y %H:%M:%S', timezone='UTC')
bd <- unclass(bd)
bd[['year']] + 1900 # yılı aldık
bd[['mon']] + 1 # ay


birth_date <- '23/06/2000 10:00:00'
bd <- as.POSIXlt(birth_date, format='%d/%m/%Y %H:%M:%S', timezone='UTC')
bd$year + 1900 # yılı aldık. unclass yapmazsak da kullanabiliriz
bd$mon + 1 # ay
