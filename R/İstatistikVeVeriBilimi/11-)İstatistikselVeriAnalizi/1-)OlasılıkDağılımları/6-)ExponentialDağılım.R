# Üstel dağılım; belirli bir olay meydana gelene kadar geçen süre ile ilgilenen
# bir sürekli olasılık dağılımıdır.
# Örneğin; bir otobüs durağından 10 dakikada bir otobüs geçiyor. Bu durakta otobüsün
# belirli bir zaman anında bir dakikadan daha geç gelmesinin olasılığını veren dağılım
# üstel dağılımdır.

# Poisson dağılımı ile aynı parametreyi; Lambda'yı kullanırlar. Fakat; poisson sabit
# bir zaman aralığına göre bir olayın belirli sayıda meydana gelme olasılığını hesaplarken
# üstel dağılım sabit zaman aralıklarıyla gerçekleşen olaylarda bir sonraki olay
# ne zaman ve ne kadar olasılıkla meydana gelmesiyle ilgilenmektedir.

# f(x) = λ {e}^{- λ x}

?dexp



# Soru:
## Bir otobüs durağına 10 dakikada bir otobüs gelmektedir. Bu durumda;
## Poisson Problemi: Bir dakika sonra otobüs gelmeme olasılığı nedir?
## Üstel Problemi: Otobüsün gelmesinin bir dakikadan daha uzun sürmesi olasılığı nedir?

## Lambda = 1/10 olur bu problem için

#Cevaplar
### Poisson Problemi
dpois(x=0,lambd=1/10) # 10 dakikada 1 otobüs geliyorsa, 0 otobüs gelme olasılığı nedir

### Üstel Problemi
pexp(q = 1, rate = 1/10, lower.tail = F)




dexp(x = 2, rate=1/10) # 10 dakikada 1 otobüs gelen durakta 2. dakikada otobüs gelme olasılığı

plot(1:30,dexp(1:30,rate=1/10),bty='L',pch=19,col='orange')




# kümülatif olasılık
pexp(q=5,rate=1/10,lower.tail = T) # 10 dakikada 1 gelen otobüsün 5 dakika veya daha az olma sürede gelme olasılığı
pexp(q=5,rate=1/10,lower.tail = F) # 10 dakikada 1 gelen otobüsün 5 dakikadan daha fazla sürede gelme olasılığı


# verilen olasılığa göre zamanı bulma
qexp(p=0.3, rate=1/10, lower.tail = F) # kaçıncı dakikadan sonra 10 dakikada 1 geçen otobüs gelir
qexp(p=0.3, rate=1/10, lower.tail = T) # kaçıncı dakikadan önce 10 dakikada 1 geçen otobüs gelir


# rastgele veriler üretmek
rexp(n=10,rate=1/10) # 10 dakikada 1 geçen otobüs için 10 adet kaçıncı dakikada gelme değerleri





































