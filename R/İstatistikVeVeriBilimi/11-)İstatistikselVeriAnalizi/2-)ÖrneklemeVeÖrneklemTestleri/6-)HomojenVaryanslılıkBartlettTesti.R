# veriler sürekli olmalıdır
# normal dağılım göstermeleri gerekir
# gruplar bazında bakarız
df <- subset(iris,subset = (Species != 'setosa'))
shapiro.test(df$Sepal.Width[df$Species == 'versicolor'])
shapiro.test(df$Sepal.Width[df$Species == 'virginica'])

boxplot(df$Sepal.Width ~ as.character(df$Species))


# H0: Varyanslar homojendir
# H1: Varyanslar homojen değildir
# p-value > 0.05 ise H0 hipotezi reddedilemez
bartlett.test(df$Sepal.Width ~ as.character(df$Species))
