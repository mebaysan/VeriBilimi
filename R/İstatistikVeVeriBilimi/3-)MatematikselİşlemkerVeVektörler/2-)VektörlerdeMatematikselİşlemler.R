x <- c(12,43,67,45,32,78)

# pandas'a benzer vektör atanmış bir değişkende matematiksel işlem yaparsak vektörün tüm elemanlarına uygular

x + 2 

sqrt(x) # her elemanın karekökünü alır


vek1 <- c(1:10) 
vek2 <- c(11:20)

vek1 + vek2 # 2 vektördeki elemanları karşılıklı olarak toplar


# en doğru seçim vektör vektöre toplarken vektörlerin eleman sayısı eşit olmalıdır
# veya uzun olan vektörün eleman sayısı kısa olan vektörün eleman sayısının katı olması gerekir

x <- c(12,13,14,15)
y <- c(3,2)
x+y # bu işlemde hata/uyarı almayız. İndislere göre -> [1 + 1] [2 + 2] [3 + 1] [4 + 2]

x <- c(12,13,14)
y <- c(3,2)
x + y # uyarı alırız. eleman sayıları birbirine eşit olmazsa baştaki indise gider ve toplamaya oradan devam eder
# 12 + 3
# 13 + 2
# 14 + 3

