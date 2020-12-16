# Jacob Bernoulli tarafından bulunmuştur
# Kesikli olasılık dağılımıdır
# Tek denemede gerçekleşen olayların olasılığının hesaplanmasında kullanılır
# Denemeler 2 sonuca sahiptir (Yazı-Tura, 0-1)

# p = Başarılı olma olasılığı
# q = Başarısız olma olasılığı
# 1 - p = q
# p + q = 1
# x = Denemeler => (0,1,1,0,0,1,1)

# FORMÜL:
## p(x) = p^x (1-p)^(1-x)
## Örnek: Yazı-Tura, Yazı gelme olasılığımız 0.5'tir (başarılı olma olasılığı)

px <- (0.5 ** 0) * ((1-0.5)**1-0)
px

install.packages('Rlab')
library(Rlab)

?dbern()


# Başarılı olma olasılığı 0.6
dbern(x = 0, prob=0.6) # x -> gelmesini istediğim değer (Mesela Tura), prob -> 0 (Tura) gelme olasılığı

dbern(x=1,prob=0.7) # direkt 0.7'i verir çünkü x = 1'dir

# Bir torbada 6 siyah 4 beyaz olmak üzere 10 top vardır. Siyah top çekme olasılığım nedir? Bu durumda Siyah top alma durumumuz 1'dir. x = 1
dbern(x=1,prob = 0.6) # Siyah top çekme olasılığı
dbern(x=0,prob = 0.6) # Beyaz top çekme olasılığı

# kümülatif olasılık hesaplar
pbern(q = 1, prob = 0.6, lower.tail = T) # başarılı olma olasılığının 0.7 olduğu bir değerde 1 ve 1'den daha az olma olasılığı (lower.tail = T)


pbern(q = 1, prob = 0.6, lower.tail = F) # 1'den daha fazla olma olasılığı
pbern(q = 0, prob = 0.6, lower.tail = F) # 0'dan daha fazla olma olasılığı



qbern(p=0.5, prob = 0.7, lower.tail = T) # 0.7 olasılıkla 0.5'e eşit veya daha küçük bir değer elde edebiliriz
qbern(p=0.2,prob=0.7,lower.tail = T)





# rasgele bernouilli dağılan veriler oluşturur
rbern(n = 50, prob = 0.7) # 50 adet değer 0.7 başarılı olma olasılığı ile

















































