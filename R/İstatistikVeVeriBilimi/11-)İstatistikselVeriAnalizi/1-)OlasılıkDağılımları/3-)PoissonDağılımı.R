# Belirli bir aralıkta (alan, hacim, uzunluk, zaman) istenilen olayın belirli bir sayıda olma olasılığı ile ilgilenir
# Sonlu bir olasılık dağılımıdır
# 1 saat içinde köprüden geçen arabaların sayısı, hastanede bir günde 2 saat arasında doğan çocuk sayısı, bir gün içinde metrobüs kullanan insanların sayısı vb.

# Bütün eylemler birbirinden bağımsız olmalıdır
# Ortalama olay zamanı sabittir, her bir olay için zaman aralığı sabit olmalıdır
# İki olay aynı anda gerçekleşemez

# p(x) = λ^x exp(-λ)/x!

# λ -> belirli bir dilimde ölçüm yaptığımız birim adedi (Örn: 1 saatte köprüden geçen arabalar örneği için λ = 1 saatte geçen araba sayısı)
# x -> istediğimiz olayın gerçekleşme sayısı


?dpois


# bir saatte köprüden ortalama 15 araba geçiyor;
## 1-) bu köprüden bir saatte 20 araba geçme olasılığı (tam 20)
dpois(x = 20, lambda = 15)
## 2-) bu köprüden bir saatte 5 araba geçme olasılığı
dpois(x = 5, lambda=15)


plot(1:30, dpois(1:30, lambda=15),col='orange',pch=19) # 1'den 30'a kadar arabaların geçme olasılığı
lines(dpois(1:30,15), lwd=2, col='blue')


# 1 saatte 20 araba geçiyor
## 1 dakikada 20/60 geçiyordur
dpois(x=2, lambda = 20/60) ## dakikada 2 araba geçme olasılığı




# Kümülatif olasılık
## 1 saatte 20 araba geçiyor; 1 dakikada 20/60 geçiyordur
ppois(q=3, lambda=20/60,lower.tail = T) # bir dakikada 0,1,2,3 araba geçme olasılığı
ppois(q=3, lambda=20/60,lower.tail = F) # bir dakikada 3'ten fazla geçme olasılığı





# Olasılık değerine göre x değerini elde etmek
qpois(p=0.6, lambda = 15, lower.tail = T) # 1 saatte 15 araba geçen köprüden %60 olasılıkla kaç araba geçer (x veya x'den daha az)
qpois(p=0.2,lambda=15,lower.tail = F) # 1 saatte 15 araba geçen köprüden %20 olasılıkla kaç araba geçer (x'den daha fazla)





# rassal değişkenler üretmek
rpois(n=10,lambda=15) # ölçüm aralığının birim ortalaması 15'e göre 10 sayı üret

rpois(n=50,lambda=25) # 1 saatte ortalama 25 araba geçen köprüden geçebilecek araba sayısı




# Soru:
## Bir fabrikanın ürettiği pillerin %1'i kusurlu çıkarsa, 200 ünitelik üretimde üç kusurlu pil çıkması olasılığı nedir?
# Çözüm:
## Lambdayı bulmak için 200 * 0.01 yaparız. Ortalama %1'lik hata ile 200 ünitede hata yapma olasılığını buluruz
lmb = 200 * 0.01
## lmb bizim lambda değerimiz oldu, 200 ünitedeki hata olasılığı. Şimdi 3 hatalı bulmak için poisson dağılımdan faydalanırız
dpois(x=3,lambda=lmb) # cevap

































