start_date = as.Date('23/06/2000', format='%d/%m/%Y')
end_date = Sys.Date()

dates <- seq.Date(from=start_date, to=end_date, by='year')

dates[dates<as.Date('23/06/2010',format='%d/%m/%Y')] # vektörde 2010'dan küçük değerler

dates[dates<as.Date('23/06/2010',format='%d/%m/%Y')] # vektörde 2010'dan küçük değerler


date_time <- as.POSIXlt(dates) # tarihleri datetime (tarih zaman) formatına çeviriyoruz

date_time[date_time$year+1900 == 2010] # 2010 yılına ait verileri filtrele


which(date_time$year+1900 == 2010) # 2010 yılına ait verilerin indisini verir

indis <- which(date_time$year+1900 == 2010)
date_time[indis]

date_time[date_time$year+1900 > 2010 & date_time$year+1900 < 2018] # 2010'dan büyük ve 2018'den küçük veriler
