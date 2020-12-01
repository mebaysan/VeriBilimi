x <- c(12,32,123,45,12,23,4,5,6,7,99)

x[1] # 1. elemanı seçtik

x[-1] # 1. eleman çıktı fakat bu kalıcı değil, bunu tekrar atamamız gerekir

x = x[-1] # şimdi 1. indis vektörden çıkarıldı
x

length(x) # x vektörünün eleman sayısı

x[-8] # 8. indis çıkarıldı

y <- x[-8] # x'ten 8. indis çıkarılıp y'e atanıyor

x;y # 2 değişkeni birden çalıştırdık


x[-c(3,4,5)] # 3,4 ve 5. indisleri vektörden çıkartır


cikacaklar <- c(2,4,6) # bir değişkene atadık
x[-cikacaklar]

1:3 # 1'den 3'e kadar bir seri oluşturur

x[-c(1:3)] # ardışık indisleri (seri) çıkartmak
