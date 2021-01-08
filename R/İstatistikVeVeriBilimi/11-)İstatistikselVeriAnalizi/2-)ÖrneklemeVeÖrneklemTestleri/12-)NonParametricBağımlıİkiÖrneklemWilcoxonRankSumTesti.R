# Wilcoxon Rank Sum testidir. Literatürde Mann-Whitney U Testi olarak da geçer.
# veri seti: https://drive.google.com/drive/folders/1-wllHNuemFKbi5JAPle-K4zxBoGUTB77  (InstPostComparison)
ins <- read.csv('InsPostComparison.csv')
View(ins)

par(mfrow=c(1,2))
hist(ins$RPostsViewed)
hist(ins$LPostsViewed)

shapiro.test(ins$RPostsViewed)
shapiro.test(ins$LPostsViewed)
# Değişkenlerin normal dağılım göstermediğini görüyoruz


median(ins$RPostsViewed)
median(ins$LPostsViewed)


?wilcox.test()

# H0: 2 değişkenin medyanları arasında fark yoktur
# H1: 2 değişkenin medyanları arasında fark vardır
wilcox.test(ins$LPostsViewed,ins$RPostsViewed,
            mu=0,
            paired=T # bağımlı değişkenler olduğundan
            )


# H0: 2 değişkenin medyanları arasında fark 10'dur
# H1: 2 değişkenin medyanları arasında fark 10'dan farklıdır
wilcox.test(ins$LPostsViewed,ins$RPostsViewed,
            mu=10,
            paired=T 
)




wilcox.test(ins$LPostsViewed,ins$RPostsViewed,
            mu=10,
            paired=T,
            conf.int = T # güven aralığını göster
)






# H0: 2 değişkenin medyanları arasında fark 10'dan küçük veya eşittir
# H1: 2 değişkenin medyanları arasında fark 10'dan büyüktür
wilcox.test(ins$LPostsViewed,ins$RPostsViewed,
            mu=10,
            paired=T,
            conf.int = T,
            alternative = 'greater'
)







# H0: 2 değişkenin medyanları arasında fark 10'dan büyük veya eşittir
# H1: 2 değişkenin medyanları arasında fark 10'dan küçüktür
wilcox.test(ins$LPostsViewed,ins$RPostsViewed,
            mu=10,
            paired=T,
            conf.int = T,
            alternative = 'less'
)





