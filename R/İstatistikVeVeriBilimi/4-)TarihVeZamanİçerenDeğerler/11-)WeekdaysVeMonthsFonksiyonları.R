date_times <- seq(
  from=strptime('23/06/2000',format='%d/%m/%Y'),
  to=strptime('23/06/2020',format='%d/%m/%Y'),
  by='quarter')

date_times


sessionInfo()
Sys.setlocale('LC_TIME','tr_TR.UTF-8') # local sistem dilini değiştiririz (türkçe)

weekdays(date_times) # vektörün elemanlarının hangi güne denk geldiğini söyler

months(date_times) # vektörün elemanlarının hangi aya denk geldiğini söyler

df <- data.frame('Date'=date_times,'Month'=months(date_times),'Day'=weekdays(date_times))
df


Sys.setlocale('LC_TIME','en_US.UTF-8') # local sistem dilini ingilizce olarak set ettik
