# Saçılım diyagramı - scatter plot

View(airquality)


plot(airquality$Ozone) # x ekseni indisleri, y ekseni değerleri gösterir




plot(airquality$Ozone, bty='L') # bty parametresi sayesinde L şekline getirebiliriz


plot(airquality$Ozone, pch=19) # pch parametresi sayesinde pointerleri değiştirebiliriz
plot(airquality$Ozone, pch='-')
?pch


plot(airquality$Ozone, type='h') 
# saçılım diyagramını histograma benzetebiliriz

plot(airquality$Ozone, type='l') # çizgi grafik gibi gösterir

plot(airquality$Ozone, type='b',pch=19) # birbirine yakın olan noktaları birbirine bağlar

plot(airquality$Ozone, type='c',pch=19) # noktaları silip line'lar ile noktaları birbirine bağlar

plot(airquality$Ozone, type='o',pch=19) # o -> overplotting, over olan noktaları ayırır

plot(airquality$Ozone, type='s',pch=19) # adımsal gösterir



# iki değişken arasındaki ilişkiyi gösteren saçılım diyagramları
plot(airquality$Ozone,airquality$Temp,pch=19,bty='L')
# 2 değişken arasındaki ilişki

plot(airquality$Ozone,airquality$Temp,
     pch=19,bty='L',
     main='Ozone x Temp',
     xlab='Ozone',ylab='Temp'
     )


# Renkleri değiştirmek
plot(airquality$Ozone,airquality$Temp,col='red',pch=19)
plot(airquality$Ozone,airquality$Temp,col=c('red','orange'),pch=19)

## Belirli bir değere göre renklendirme
library(tidyverse)
airquality %>% distinct(Month)
class(airquality$Month)
airquality$Month <- as.factor(as.character(airquality$Month)) # değişkeni factore çevirdik
class(airquality$Month)
plot(airquality$Ozone,airquality$Temp,
     bty='L',
     col=c('blue','orange','purple','pink')[airquality$Month], # sırasıyla bu faktör değişkenine göre renk atar
     pch=19)

c('blue','orange','purple','pink')[airquality$Month]
# renklerden oluşan bir vektör oluşturur


plot(airquality$Ozone,airquality$Temp,
     bty='L',
     col=c('blue','orange','purple','pink')[airquality$Month],
     pch=19)
legend( # plot'a legend ekler
  x='topright',  # lejant konumu
  legend=levels(airquality$Month), # lejant nelerden oluşacak
  col =c('blue','orange','purple','pink'), # hangi renklerden oluşacak
  pch = 19
  )




par(mar=c(6,6,6,7), xpd=T) # grafiğe margin verir, xpd -> dışarı taşma olsun mu?
plot(airquality$Ozone,airquality$Temp,
     bty='L',
     col=c('blue','orange','purple','pink')[airquality$Month],
     pch=19)
legend(
  x='topright', 
  legend=levels(airquality$Month),
  col =c('blue','orange','purple','pink'),
  pch = 19,
  inset = c(-0.2,0) # legend konumudur, ilk parametre sağ-sol, ikinci parametre de yukarı-aşağı
)





# Noktaları değişken değerine göre boyutlandırmak

par(mar=c(6,6,6,7), xpd=T)
plot(airquality$Ozone,airquality$Temp,
     bty='L',
     col=c('blue','orange','purple','pink')[airquality$Month],
     pch=19,
     cex = 2, # cex parametresi sayesinde noktaların boyutlarını değiştirebiliriz
     )
legend(
  x='topright', 
  legend=levels(airquality$Month),
  col =c('blue','orange','purple','pink'),
  pch = 19,
  inset = c(-0.2,0)
)




par(mar=c(6,6,6,7), xpd=T)
plot(airquality$Ozone,airquality$Temp,
     bty='L',
     col=c('blue','orange','purple','pink')[airquality$Month],
     pch=19,
     cex = airquality$Wind/10, # Wind değişkenine göre noktaları boyutlandır
)
legend(
  x='topright', 
  legend=levels(airquality$Month),
  col =c('blue','orange','purple','pink'),
  pch = 19,
  inset = c(-0.2,0)
)

legend(x='topright',legend=c('Düşük','Orta','Yüksek'), 
       title='Wind', # lejanta başlık verir
       pt.cex = c(min(airquality$Wind/10), # lejanttaki noktaları boyutlandır
                  mean(airquality$Wind/10),
                  max(airquality$Wind/10)),
       pch=19,
       inset = c(-0.25,0.5)
       )



# scatter plotta Lineer Doğru ve Lowess Doğru

## lineer doğru ilişkinin yönünü verir
## lowess doğrusu noktaların nasıl dağıldığını verir

airquality <- na.omit(airquality) # veri setindeki kayıp gözlemleri çıkartır

par(mar=c(5,5,5,7.2),xpd=F) # çizgi dışarı çıkamaz
plot(x=airquality$Ozone,y=airquality$Temp,
     main='Ozon ve Sıcaklık İlişkisi',
     xlab='Ozon Değerleri',
     ylab='Sıcaklık Değerleri',
     pch=19,
     bty='L',
     col=c('blue','red','pink','orange')[airquality$Month],
     cex=airquality$Wind/10
     )
abline(lm(airquality$Temp~airquality$Ozone),lwd=2,lty='dotted',col='purple') # lineer (ilişki) doğrusu
#lm(y~x)
par(xpd=T) # lejantlar dışarı çıkabilir
legend(x='topright',legend=levels(airquality$Month),
       col=c('blue','red','pink','orange'),
       title='Aylar',
       pch=19,
       inset=c(-0.2,0))
legend(x='topright',legend=c('Düşük','Orta','Yüksek'),
       pch=19,
       cex=0.8,
       pt.cex=c(0.2,0.9,2),
       title='Rüzgar Seviyeleri',
       inset=c(-0.25,0.6))
lines(
  lowess(airquality$Ozone,airquality$Temp), # na değerler varsa hata verecektir
  lty='dotted',col='green',lwd='2')
























































