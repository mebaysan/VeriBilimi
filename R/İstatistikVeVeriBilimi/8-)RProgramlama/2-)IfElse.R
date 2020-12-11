x <- 6

if (x / 2 == 0) {
  cat('x değişkeni (',x,') çift sayıdır')  
}else{
  cat('x değişkeni (',x,') tek sayıdır')  
}


y <- rnorm(100,mean=5,sd=8)

if (mean(y) == 5) {
  print('Ortalama 5')
}else{
  print('Ortalama 5 değil')
}

mean(y)

z <- 3
ifelse(z < 5, 'DOĞRU','YANLIŞ') # single line ifelse -> ilk paramtre doğru ise 2. parametreyi yaz, değil ise 3. parametreyi yaz
# & -> VE
# | -> VEYA