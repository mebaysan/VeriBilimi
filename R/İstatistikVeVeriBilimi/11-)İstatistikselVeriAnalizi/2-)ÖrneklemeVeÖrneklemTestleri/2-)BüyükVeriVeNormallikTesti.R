# Dataset: https://www.kaggle.com/spscientist/students-performance-in-exams

df <- read.csv('StudentsPerformance.csv')
View(df)

cat('Satır sayısı:',nrow(df))
cat('Sütun sayısı:',ncol(df))

hist(df$math.score)
# H0: Dağılım normaldir
# H1: Dağılım normal değildir
# p > 0.05 ise H0 reddedilemez (%95 güven)
shapiro.test(df$math.score)


clean <- df$math.score[-which(df$math.score < 30)] # değeri 30'dan küçük olanları çıkar
hist(clean)
shapiro.test(clean) # histogram normal dağılıyorken neden shapiro normal dağılmıyor dedi (büyük sayıda veriler için shapiro çok doğru sonuçlar vermemektedir)

shapiro.test(clean[1:100])
shapiro.test(clean[100:200])
shapiro.test(clean[200:300])
shapiro.test(clean[300:400])
shapiro.test(clean[400:500])
shapiro.test(clean[500:600])
shapiro.test(clean[600:700])
shapiro.test(clean[700:800])
shapiro.test(clean[800:900])
shapiro.test(clean[900:1000])


smp <- sample(clean,100) # 100 örnek aldık
shapiro.test(smp) # aldığımız 100 örnek üzerinde shapiro uyguladık




p.valueler = numeric(50) # 50 elemanlı bir vektör oluştur
for(i in 1:50){
  smp <- sample(clean,100) # 100 örneklem çek
  p.val <- shapiro.test(smp) # shapiro testi uygula
  p.valueler[i] = p.val$p.value # vektörün i. elemanını p value olarak ayarla
}
mean(p.valueler) # rastgele 50 shapiro testinin ortalaması 0.05'den büyükse veriler normal dağılıyordur















