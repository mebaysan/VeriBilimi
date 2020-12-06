# %d - day as a number (0-31) -> 01-31
# %a - abbreviated weekday -> Mon
# %A - unabbreviated weekday -> Monday
# %m - month (00-12) -> 00-12
# %b - abbreviated month -> Jan
# %B - unabbreviated month -> January
# %y - 2 digit year -> 07
# %Y - 4 digit year -> 2007


Sys.Date() # bugünün tarihini verir

today <- Sys.Date()
class(today)


tarih <- '23/06/2000'

yeni_tarih <- as.Date(tarih, format = '%d/%m/%Y') # gelen stringi hangi türde formatlayıp Date'e çevireceğiz
class(yeni_tarih)


tarih <- '23-06-2000'
as.Date(tarih,format='%d-%m-%Y')
