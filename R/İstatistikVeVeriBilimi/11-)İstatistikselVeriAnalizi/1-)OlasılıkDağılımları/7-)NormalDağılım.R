# Normal olasılık dağılımı, belirli bir ortalama veya standart sapma değerine sahip
# popülasyonda elde edilebilecek değerlerin olasılığını veren sürekli bir dağılımdır

# f(x) = 1/(√(2 π) σ) e^-((x - μ)^2/(2 σ^2))

?dnorm


dnorm(x = 20, mean = 30, sd= 5) # ortalaması 30 standart sapması 5 olan popülasyondan 20 gelme olasılığı
dnorm(x = 30, mean = 30, sd= 5) # ortalaması 30 standart sapması 5 olan popülasyondan 30 gelme olasılığı
plot(1:60,dnorm(x=1:60,mean=30,sd=5), bty='L',pch=19,col='orange') # çan eğrisi oluştu, veriler normal dağılmıştır



# Soru:
## Bir sınıftaki öğrencilerin boy ortalaması 180 cm'dir ve standart sapması 10 cm'dir.
## Rastgele seçilen öğrencinin boyunun 160 cm'den daha fazla olma olasılığı nedir?
pnorm(q=160, mean=180, sd=10,lower.tail = F) # boyu 160 cm'den daha fazla olma olasılığı
pnorm(q=160, mean=180, sd=10,lower.tail = T) # boyu 160 cm'e eşit veya daha az olma olasılığı

pnorm(q=180, mean=180, sd=10,lower.tail = T) # boyu 180 cm'den daha fazla olma olasılığı


# x değerini elde etmek
qnorm(p = 0.3, mean=180,sd=5,lower.tail = F) # boy ortalaması 180 cm, standart sapması 5 cm olan sınıftan 0.3 olasılıkla ne kadardan daha fazla bir değer elde ederim
qnorm(p = 0.3, mean=180,sd=5,lower.tail = T) # boy ortalaması 180 cm, standart sapması 5 cm olan sınıftan 0.3 olasılıkla ne kadara eşit veya daha az bir değer elde ederim



# rastgele normal dağılan değerler üretmek
rnorm(n=10,mean=180,sd=5) # ortalaması 180 standart sapması 5 olan 10 değer üret

hist(rnorm(n=50,mean=50,sd=5))

