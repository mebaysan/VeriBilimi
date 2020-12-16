# Başarı olasılığı olan bir Bernoulli denemesinin aynı şartlar altında n kez tekrarlanması ile oluşan deneye binom deneyi denir
# Denemeler birbirinden bağımsızdır. Her denemede iki olası sonuç vardır (istenen ve istenmeyen olay)
# p + q = 1
# 1 - p = q
# n -> deneyin kaç kere tekrarlandığı
# x -> başarılı olma sayısı (ne kadar başarılı olmak istiyoruz)
# p -> istediğimiz olayın olasılığı
# q -> istemediğimiz olayın olma olasılığı
# p(x) = choose(n, x) p^x (1-p)^(n-x)

?dbinom


# 0.3 başarılı olma olasılığı olan bir olayda
dbinom(x = 9, size=10, prob=0.3) # tekil olarak oalsılıkları bulur
# x -> kaç kere başarılı olmak istiyorum
# size -> kaç kere deneyi gerçekleştireceğim
# prob -> başarılı olma olasılığım nedir


dbinom(x = c(1:30), size = 30, prob = 0.7)
# 1'den 30'a kadar her sayı için başarılı olma olasılığı 0.7 olan 30 deney yap ve her seferinde başarılı olmak istediğim sonuç sayısı  x olsun 

plot(x = 1:30, y = dbinom(x = c(1:30), size = 30, prob = 0.7),
     vty = 'L',
     pch=19)
lines(dbinom(x = c(1:30), size = 30, prob = 0.5))

pbinom() # kümülatif olarak verir

pbinom(q = 5, size = 30, prob = 0.5,lower.tail = T) # 5 ve 5'ten daha az başarılı olma olasılığı
pbinom(q = 5, size = 30, prob = 0.5,lower.tail = F) # 5'ten daha fazla başarılı olma olasılığı


pbinom(q = 3, size = 30, prob = 0.2,lower.tail = T) # Meali => başarı şansı 0.2 olan bir deneyi 30 kere art arda tekrarlarsam 1,2 veya 3 kere başarılı olma olasılığım nedir?
# lower.tail = T -> q ve q'dan daha küçük

pbinom(q=3,size=30,prob=0.5,lower.tail = T) # alttaki 4 fonksiyon ile eşittir (kümülatif)
dbinom(x = 0, size = 30, prob=0.5) + 
dbinom(x = 1, size = 30, prob=0.5) + 
dbinom(x = 2, size = 30, prob=0.5) + 
dbinom(x = 3, size = 30, prob=0.5)



# Örnek
# bir e-ticaret sitesine gelen ortalama 4 müşteriden 1'i alış veriş yapıyor
# bu e-ticaret sitesine bir gün için 30 müşteri girmesi bekleniyor
# en az 10 alış veriş yapılma olasılığı nedir
pbinom(q = 9, size = 30, prob = 0.25, lower.tail = F)
# lower.tail = T -> q'dan daha fazla olanlar
plot(x = 1:30, y = dbinom(x = 1:30, size=30 ,prob=0.25))
lines(dbinom(x = 1:30, size=30 ,prob=0.25))
## cevap -> 0.1965934


# Olasılık değerine göre n denemede kaç kere başarılı olacağız
qbinom(p=0.3,size=30,prob=0.25,lower.tail = F) # 0.3 olasılıkla 30 müşteriden (0.25 satın alma oranıyla) 9'dan fazlası alış veriş yapar
qbinom(p=0.3,size=30,prob=0.25,lower.tail = T) # 0.3 olasılıkla 30 müşteriden (0.25 satın alma oranıyla) 6 ve daha  az müşteri alış veriş yapar



# rastgele binom dağılan veriler
rbinom(n=50,size=30,prob=0.25) # 0.25 olasılıkla 30 müşteriden kaç tanesi alış veriş yapar (istenen olay) için 50 adet binom veri üret
hist(rbinom(n=50,size=30,prob=0.25))


dbinom(x = 9, size = 10, prob = 0.5)




















