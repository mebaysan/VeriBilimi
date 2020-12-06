library('chron')

date_times <- seq(
  from=strptime('23/06/2000 12:15:25',format='%d/%m/%Y %H:%M:%S',tz='UTC'),
  to=strptime('23/06/2020 12:15:25',format='%d/%m/%Y %H:%M:%S',tz='UTC'),
  by='year')

date_times


dates <- format(date_times, format='%d/%m/%Y') # sadece tarihleri aldık
dates
dates <- as.Date(dates, format='%d/%m/%Y') # tarih formatına çeviririz
dates



times <- format(date_times, format('%H:%M:%S')) # sadece zamanları aldık
times
times <- times(times,format='h:m:s') # zamanları formatladık (chron fonksiyonu sayesinde)
times

df <- data.frame('Date'=dates,'Times'=times) # bir veri çerçevesi oluşturuyoruz
df

df$Date
df$Times

df$Date[1] - df$Date[2]
