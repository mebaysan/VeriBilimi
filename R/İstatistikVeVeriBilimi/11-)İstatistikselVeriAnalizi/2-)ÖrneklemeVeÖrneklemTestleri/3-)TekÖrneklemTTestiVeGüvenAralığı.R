# T dağılım; normal dağılımın standart sapmasının biraz daha fazla olduğu dağılımdır
# biraz daha yayvandır (yaklaşık normal dağılım)
# sürekli veriler için uygulanır
# Örneklem üzerinden popülasyona ilişkin çıkarımlar yapılmaya çalışılır
# p-value 0.05'den büyük ise H0 kabul edilir


View(iris)
hist(iris$Sepal.Length)

shapiro.test(iris$Sepal.Length) # yaklaşık normal dağıldığını görebiliriz

help(t.test)

# H0: Örneklem Ortalaması = Test Değeri
# H1: Örneklem Ortalaması != Test Değeri
t.test(
  iris$Sepal.Length,
  mu=3, # değişkenin ortalama değeri 3'e eşittir (Hipotez)
  alternative = 'two.sided', # Eşitlik üzerinden hipotez kurulur
  conf.level = 0.95 # güven aralığı
  )

# H0'da her zaman eşitlik vardır (= >= <=)

# H0: Örneklem Ortalaması >= Test Değeri
# H1: Örneklem Ortalaması < 3 Test Değeri
t.test(
  iris$Sepal.Length,
  mu=3, # değişkenin ortalama değeri 3'e büyük veya eşittir (Hipotez)
  alternative = 'less', # H1 küçüktür
  conf.level = 0.95
)




# H0: Örneklem Ortalaması <= Test Değeri
# H1: Örneklem Ortalaması > 3 Test Değeri
t.test(
  iris$Sepal.Length,
  mu=3, # değişkenin ortalama değeri 3'e küçük veya eşittir (Hipotez)
  alternative = 'greater', # H1 büyüktür
  conf.level = 0.95
)




t.test(
  iris$Sepal.Length,
  mu=5.8,
  alternative = 'two.sided',
  conf.level = 0.95
) # bu teste göre H0 hipotezi red edilemez (ortalama 5.8'e eşittir). 
# Bu test aslında mu değerinin confidence interval'e olan uzaklığını ölçüyor gibi düşünebiliriz




















