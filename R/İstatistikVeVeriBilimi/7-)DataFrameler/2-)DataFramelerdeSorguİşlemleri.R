df <- data.frame('A'=rnorm(100,mean=10,sd=2),'B'=rnorm(100,mean=5,sd=4),'C'=rnorm(100,mean=12,sd=4))
df



df$A < 8 # logical olarak A değişkeninin 8'den küçük değerlerini bize gösterir


which(df$A < 8) # bize A değişkeni 8'den küçük olan değerlerin indisini vektör olarak verir



idx <- which(df$A<8)
df[idx,] # dataframelerde 'satır,sütun' olarak seçim yaparız. virgülün soluna satır, sağına sütun yazılır



df[idx,c('B','C')] # A'nın 8'den küçük olduğu gözlemlerin B ve C değişlenlerini seç



df[which(df$B < mean(df$B)),c('A')] # B'nin kendi ortalamasından küçük olan gözlemlerin A değişkenini getir

