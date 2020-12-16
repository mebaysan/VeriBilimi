# n farklı çıktının eşit olasılıkla meydana gelebileceği olasılık dağılımıdır.
# Uniform dağılımına örnek olarak zar atma deneyi verilebilir.
# Uniform dağılımı hem kesikli hem de sürekli olabilmektedir.
# serinin tüm elemanlarının seçilme şansı eşittir


# f(x) = 1/(max-min)



?dunif

zar <- c(1:6)

dunif(x=3,min=min(zar),max=max(zar)) # 1 ile 6 arasındaki bir seriden 3 gelme olasılığı



plot(1:20,dunif(1:20,min=1,max=20))


punif(q=5,min=1,max=15,lower.tail = T) # 1 ile 15 arasındaki bir seriden 5 ve 5'ten daha az bir değer gelmesi
punif(q=5,min=1,max=15,lower.tail = F) # 1 ile 15 arasındaki bir seriden 5'ten daha fazla bir değer gelmesi




# Olasılık değerine göre hangi değeri elde edebileceğimizi verir
qunif(p=0.6,min=1,max=6, lower.tail = T) # 0.6 olasılıkla değeri 4 veya daha az eleman gelir

qunif(p=0.6,min=1,max=6, lower.tail = F) # 0.6 olasılıkla değeri 3'ten daha fazla eleman seçersin



# rastgele değerler üretmek
runif(n=10, min=1, max=6) # 1 ile 6 arasındaki seriden 10 adet rastgele değer üret
round(runif(n=10,min=1,max=6))



# Soru:
## Kombi tamir eden bir firma, bir kombinin genelde 1.5 saat ile 4 saat arasında
## tamir edildiğini bilmektedir. Bu koşullarda rassal olarak seçilen bir kombinin
## tamirinin 2 saatten fazla olma olasılığı nedir?
punif(q=2,min=1.5,max=4,lower.tail = F)

## Tamirinin 3 saatten az olması olasılığı nedir
punif(q=3,min=1.5,max = 4, lower.tail = T)

# Tamir sürelerinin %30'unun en uzun süresi ne kadardır?
qunif(p=0.3,min=1.5, max=4)












































































