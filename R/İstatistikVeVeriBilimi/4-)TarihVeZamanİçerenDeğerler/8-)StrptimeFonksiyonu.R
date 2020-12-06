# https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/strptime

date <- '23/06/2000'

x <- strptime(date,format = '%d/%m/%Y') # strptime ile tarih değerini Date tipine çeviririz
class(x)

x$year + 1900 
