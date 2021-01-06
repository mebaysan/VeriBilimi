# H0: Dağılım = Normal Dağılım
# H1: Dağılım != Normal Dağılım
# p > 0.05 H0 Hipotezi Reddedilemez (%95 güven düzeyi)

View(iris)

hist(iris$Sepal.Length)

class(shapiro.test(iris$Sepal.Length))

shapiro.test(iris$Sepal.Length) # değişkene shapiro wilk testini uygular
# p-value 0.05'ten küçük olduğu için veriler normal dağılmıyordur (H1)

par(mfrow=c(1,2))
hist(iris$Sepal.Length)
hist(iris$Sepal.Width)

petalLengthP = shapiro.test(iris$Petal.Length)['p.value'][[1]]
if (petalLengthP > 0.05) {
  cat('p-value',petalLengthP,'olduğundan H0 hipotezi reddedilemez')
}else{
  cat('p-value',petalLengthP,'olduğundan H0 hipotezi reddedilir')
}



