#group_by fonksiyonu sayesinde gruplama yaparız


group_by(iris,Species)


df <- iris %>% group_by(Species)

print(df, n=150) # 150 satır göster



iris$extra <- c(rep('A',30),rep('B',30),rep('C',30),rep('D',30),rep('E',30))

my_func <- function(x){ # x vektörü alıyor
  max(x) - min(x) # vektörün max elemanı ile min elemanını çıkarıyor
}

iris %>% group_by(Species,extra) %>% summarise(
  SepalLengthOrtalama=mean(Sepal.Length), # Sepcies ve extra'ya göre gruplanmış verilerin SepalLength ortalamaları
  KendiFonksiyonum=my_func(Sepal.Length) # Sepal.Length vektörünü gönderiyoruz
) 

