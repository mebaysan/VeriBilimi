# Popülasyonun dağılımı ne olursa olsun yeterli sayıda örnek alındığında alınan
# örneklemin verilerinin normal dağıldığını savunmaktadır.

# Popülasyondan alınan örneklemin normal dağılım göstermesi için en az 30 veriye ihtiyaç vardır


z <- c(10,15,14,18,10,23,23,23,56,34,13,19,19,45,45,34) # normal dağılmayan veriler
hist(z) # normal dağılmayan veriler

sample(z,size=4,replace = F)

sonuclar = numeric()
for (i in 1:50) {
  ornek <- sample(z,4) # her devirde bir örneklem seç
  sonuclar <- append(sonuclar,mean(ornek)) # örneklerin ortalamasını al ve sonuclar vektörüne ekle
  
}
hist(sonuclar) # merkezi limit teoremine göre örneklemlerin ortalaması normal dağılı

par(mfrow=c(1,2)) # 1 satır 2 sütun grafik
hist(z)
hist(sonuclar)
