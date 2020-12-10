df <- read.csv('CSV__singapore.csv')
View(df)


summary(df) # özet bilgileri verir


any(is.na(df$price)) # hiç NA değer var mı içinde
mean(df$price)

sd(df$price) # price değişkeninin standart sapma

median(df$price) # medyan değerini verir
# medyan ortalamadan küçükse veriler sağa çarpıktır


hist(df$price[df$price<=1000]) # price'ı 1000'den küçük olan değerlerin histogramı


sd(df$price)
var(df$price) # price değişkeninin varyansı

min(df$price)
max(df$price)

table(df$room_type) # room_type değişkeninin frekans tablosu


quantile(df$price,probs = c(0.25,0.50,0.75)) # çeyreklikleri bize verir
