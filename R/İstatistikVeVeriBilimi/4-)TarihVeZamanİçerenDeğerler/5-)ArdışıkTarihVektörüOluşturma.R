
start_date = as.Date('23/06/2000', format='%d/%m/%Y')
end_date = Sys.Date()

seq.Date(from=start_date, to=end_date, by=1) # 1'er gün artırır. by parametresi gün olarak artırır

seq.Date(from=start_date, to=end_date, by='day') # gün gün artırır
seq.Date(from=start_date, to=end_date, by='month') # ay ay artırır
seq.Date(from=start_date, to=end_date, by='year') # yıl yıl artırır
seq.Date(from=start_date, to=end_date, by='quarter') # 3ay 3ay artırır (çeyreklik)


seq(from=start_date, to=end_date, by='quarter') # direkt seq fonksiyonu ile de ardışık tarihleri oluşturabiliriz




# Ardışık zaman değerleri
start_time = as.POSIXct('23/06/2000 10:30:00', format='%d/%m/%Y %H:%M:%S')
end_time = Sys.time()

seq.POSIXt(from=start_time, to=end_time, by=15) # 15 saniye olarak artırır
seq.POSIXt(from=start_time, to=end_time, by='hour') # 1'er saat artırır
seq.POSIXt(from=start_time, to=end_time, by='month') # 1'er ay artırır
seq.POSIXt(from=start_time, to=end_time, by='year') # 1'er yıl artırır
