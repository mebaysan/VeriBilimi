start_date = as.Date('23/06/2000', format='%d/%m/%Y')
end_date = Sys.Date()

dates <- seq.Date(from=start_date, to=end_date, by='year')

sort(dates) # vektörü küçükten büyüğe sıralar
sort(dates,decreasing = T) # vektörü büyükten küçüğe sıralar