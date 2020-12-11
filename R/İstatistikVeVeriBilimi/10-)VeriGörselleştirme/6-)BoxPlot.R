
View(mtcars)


boxplot(
  mtcars[,c('drat','wt')], # hangi değişkenler
  main='Box Plot',
  names=c('Drat Değişkeni','WT Değişkeni'),
  col = c('orange','purple'),
  border='red',
  pch=19,
  cex.axis=0.7, # eksenlerdeki yazıları boyutlandırır
  xlab='Değişkenler',
  ylab='Değerler',
  range=1.5, # aykırı gözlemler için değer belirleriz
  outline = T # aykırı gözlemler güzksün mü
        )


boxplot(
  mtcars$mpg~mtcars$gear, # soldaki değer bağımlı değişken sağdaki değer de bağımsız değişkendir
  main='Box Plot',
  col = c('orange','purple'),
  border='red',
  pch=19,
  cex.axis=0.9, 
  xlab='Vites (Gear) Değerleri',
  ylab='MPG Değerleri'
)
