# Levene's Test
# Tek bir bağımsız değişken üzerine uygulanmaktadır.
# Levene, Bartlett'a göre robusttur, normalliğe daha dayanıklıdır (çok bakmaz)
# Bu nedenle veriler normal dağılmazsa grupların varyans homojenliğini ölçümlemek için kullanılır.


install.packages('car') # levene testini yapabilmek için yüklememiz gereken paket
library(car)

?leveneTest

df <- subset(iris, subset = (Species != 'virginica'))

boxplot(df$Sepal.Width~as.character(df$Species))

# H0: varyanslar homojendir
# H1: varyanslar homojen değildir
# p-value > 0.05 H0 red edilemez
leveneTest(df$Sepal.Width ~ df$Species) # sol taraf bağımlı değişken sağ tarafsız bağımsız değişken
# setosa ve versicolor gruplarının Sepal.Width varyansları homojendir
