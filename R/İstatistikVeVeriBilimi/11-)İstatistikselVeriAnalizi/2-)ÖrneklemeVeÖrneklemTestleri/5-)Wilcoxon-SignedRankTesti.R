# Wilcoxon - Signed Rank Testi (işaretli sıra)
# bu test ortalamalar üzerinden değil medyan'a göre işlem yapar
# non parametrik bir testtir
# veri çeşitliliği az, veriler normal dağılmıyor ise bu test kullanılır
# p-value > 0.05 ise H0 red edilemez

View(warpbreaks)
hist(warpbreaks$breaks)
shapiro.test(warpbreaks$breaks) # p-value'ye bakarak verilerin normal olmadığını görebiliriz

?wilcox.test

#H0: Popülasyon medyanı = Test değeri (mu)
#H1: Popülasyon medyanı != Test değeri (mu)
wilcox.test(warpbreaks$breaks,
            mu=40,
            alternative = 'two.sided',
            conf.level = 0.95
            )
median(warpbreaks$breaks)





#H0: Popülasyon medyanı >= Test değeri (mu)
#H1: Popülasyon medyanı < Test değeri (mu)
wilcox.test(warpbreaks$breaks,
            mu=40,
            alternative = 'less',
            conf.level = 0.95
)




#H0: Popülasyon medyanı <= Test değeri (mu)
#H1: Popülasyon medyanı > Test değeri (mu)
wilcox.test(warpbreaks$breaks,
            mu=40,
            alternative = 'greater',
            conf.level = 0.95
)
