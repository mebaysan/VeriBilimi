# Veri sayısı arttıkça elde edilen sonucun güvenilirliği artmaktadır. 
# Bu kanun büyük verinin önemini vurgulamaktadır.


deney_yap <- function(atis){
  para <- c('Y','T') # Y ve T'den oluşan bir vektör (yani para) oluştur
  atış <- sample(para,atis,replace=T) # parametre olarak gelen atış sayısı kadar iadesiz örnek seç para vektöründen
  yazı <- table(atış)[['Y']] # Gelen Y sayısı
  tura <- table(atış)[['T']] # Gelen T sayısı
  tura / length(atış) # Tura gelme oranını yaz
}

deney_yap(10) # Para 10 kere havaya atıldı ve çıktı kadar Tura geldi
deney_yap(100) # Para 100 kere havaya atıldı
deney_yap(1000) # Para 1000 kere havaya atıldı
deney_yap(1000000) # Para 1000000 kere havaya atıldı
