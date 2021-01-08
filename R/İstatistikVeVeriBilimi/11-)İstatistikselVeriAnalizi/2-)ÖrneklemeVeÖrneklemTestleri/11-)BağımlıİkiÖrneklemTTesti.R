# Paired Sample T-Test
# veri seti: https://drive.google.com/drive/folders/1-wllHNuemFKbi5JAPle-K4zxBoGUTB77  (InstPostComparison)

ins <- read.csv('InsPostComparison.csv')
View(ins)

duration <- c(df$RPostsDuration,df$LPostsDuration)
groups <- c(rep('Rastgele',50),rep('Beğenilen',50))

df <- data.frame('duration' = duration, 'groups' = groups)
View(df)


shapiro.test(df$duration[df$groups=='Rastgele'])
shapiro.test(df$duration[df$groups=='Beğenilen'])
# 2 grup da normal dağılıma sahip

bartlett.test(df$duration~df$groups)
# homojen varyanslığı test etmek için bartlett testi kullanyıoruz (iki grup da normal dağıldığından)
# p-value > 0.05 yani H0 reddedilemez, homojen varyanslık kabul

?t.test()
# H0: 2 grup arasındaki ortalama farkı 0'dır
# H1: 2 grup arasındaki ortalama farkı 0 değildir
t.test(df$duration~df$groups,
       mu=0,
       paired = T, # örneklemler bağımlı olduğu için T
       )


# H0: 2 grup arasındaki ortalama farkı 10'dan büyük veya eşittir
# H1: 2 grup arasındaki ortalama farkı 10'dan küçüktür
t.test(df$duration~df$groups,
       mu=10,
       paired = T, # örneklemler bağımlı olduğu için T
       alternative ='less'
)


# H0: 2 grup arasındaki ortalama farkı 10'dan küçük veya eşittir
# H1: 2 grup arasındaki ortalama farkı 10'dan büyüktür
t.test(df$duration~df$groups,
       mu=10,
       paired = T, # örneklemler bağımlı olduğu için T
       alternative ='greater'
)









































































