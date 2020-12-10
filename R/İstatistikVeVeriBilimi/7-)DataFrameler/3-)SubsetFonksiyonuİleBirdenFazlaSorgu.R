data() # R içerisindeki default gelen veri setlerini görebiliriz


CO2 # veri setini yazdırır
View(CO2) # R'ın veri görüntüleyicisi ile veri setini görüntüleriz


?subset

names(CO2) # df'in değişken isimlerini verir


subset(CO2,subset=(uptake > 30 & Type == 'Quebec')) # CO2'den uptake değişkeni 30'dan büyük olan VE Type'ı Quebec olan verileri seç



subset(CO2,subset=(uptake > 30 & Type == 'Quebec'), select = c(Plant,Treatment))
# select parametresi ile hangi değişkenleri seçmek istediğimizi söyleyebiliriz


subset(CO2,subset=(uptake > 30  | Treatment == 'chilled')) # uptake değişkeni 30'dan büyük VEYA Treatment değişkeni chilled olan



subset(CO2,subset=((uptake > 30  & Treatment == 'chilled') | (Plant == 'Mn3')))
# (uptake'i 30'dan büyük olan VE Treatment chilled olan) VEYA Plant'i Mn3 olan gözlemleri getir

