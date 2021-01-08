# İki örneklem birbirinden bağımsız olmalıdır.
# Örneklem verileri popülasyondan rastgele olarak seçilmelidir.
# Örneklemin verileri SÜREKLİ olmalıdır.
# İki örneklemin normal dağılması gerekmektedir.
# İki örneklemin varyansları yaklaşık olarak eşit olmalıdır. Bu varsayıma homojen
#   varyanslılık varsayımı da denmektedir. Eğer bu varsayım sağlanmaz ise T-Testinin
#   varyansların eşit olduğunu varsaymayan versiyonu kullanılır.


# Bağımsız İki Örneklem T-Testi Uygulaması
df <- subset(iris, subset = (Species != 'virginica'))
View(df)
class(df)
names(df)
class(df$Species)
df$Species <- as.character(df$Species)
class(df$Species)
View(df)

par(mfrow=c(1,2))
hist(df$Sepal.Width[df$Species == 'setosa'],main='Setosa - Sepal.Width')
hist(df$Sepal.Width[df$Species == 'versicolor'],main='Versicolor - Sepal.Width')

shapiro.test(df$Sepal.Width[df$Species == 'setosa']) # H0 reddedilemez (bkz. Normallik testi 1. dosya)
shapiro.test(df$Sepal.Width[df$Species == 'versicolor']) # H0 reddedilemez
# 1. varsayım tamam -> 2 grupta normal dağılıyor


bartlett.test(df$Sepal.Width~df$Species) # Varyanslar homojendir [(H0 reddedilemez) (bkz. Bartlett test 6. dosya)]
# 2. varsayım tamam -> 2 grup arasında homojen varyanslık var

# H0: 2 grubun ortalaması arasındaki fark 0'a eşittir (bu test için/ mu=0)
# H1: 2 grubun ortalaması arasındaki fark 0'dan farklıdır
t.test(
  df$Sepal.Width~df$Species, # sola bağımlı değişken sağa bağımsız değişken, Species içindeki gruplara göre test yapar
  mu=0,
  var.equal = T # bartlet testine göre homojen varyanslık olduğundan TRUE gireriz eğer homojen varyanslık yoksa FALSE olarak belirtiriz
   )
