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


# & -> VE
# | -> VEYA