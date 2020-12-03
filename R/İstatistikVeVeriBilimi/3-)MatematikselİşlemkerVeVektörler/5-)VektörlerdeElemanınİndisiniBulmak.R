x <- seq(1,250,by=3)
x


y = 8


x == y # pandas gibi, x'in her elemanını kontrol eder y'den büyük mü


which(x == 4) # which fonksiyonu sorguya bakar ve TRUE olan İNDİSLERİ bize döner

x[which(x==4)] # x vektörünün içinden 2. indisi[which(x==4)] alır (eleman)


x[x==4] # x'ten 4'e eşit olan ELEMANLARI getirir

class(x==4)

which(x > 23) # 23'ten büyük olan elemanların İNDİSLERİ
