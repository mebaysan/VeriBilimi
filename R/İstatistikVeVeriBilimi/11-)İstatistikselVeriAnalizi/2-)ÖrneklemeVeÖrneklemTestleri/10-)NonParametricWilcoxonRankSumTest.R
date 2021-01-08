# Wilcoxon sıralı toplamlar testi
# Bu test bazı kaynaklarda "Mann-Whitney U" testi olarak da geçmektedir

# non parametrik testtir
# verilerimiz çeşitli varsayımları sağlamıyordur
# bağımsız iki örneklem T-Testinin non parametric testidir

?wilcox.test
# unutmayalım wilcoxon testinde ortalama kullanılmaz!

View(warpbreaks)

shapiro.test(warpbreaks$breaks[warpbreaks$wool == 'A']) # A grubundaki veriler normal dağılmıyor
shapiro.test(warpbreaks$breaks[warpbreaks$wool == 'B']) # B grubundaki veriler normal dağılmıyor





# H0: grupların lokasyonlarının kayması 0'a eşittir
# H1: grupların lokasyonlarının kayması 0'a eşit değildir
wilcox.test(warpbreaks$breaks~warpbreaks$wool,
            mu=0, # lokasyonlardaki kayma 0'a eşit mi değil mi
            conf.int = T
            )



# H0: grupların lokasyonlarının kayması 15'den eşit veya büyüktür
# H1: grupların lokasyonlarının kayması 15'den küçüktür
wilcox.test(warpbreaks$breaks~warpbreaks$wool,
            mu=15,
            conf.int = T,
            alternative = 'less'
)


# H0: grupların lokasyonlarının kayması 15'den eşit veya küçüktür
# H1: grupların lokasyonlarının kayması 15'den büyüktür
wilcox.test(warpbreaks$breaks~warpbreaks$wool,
            mu=15,
            conf.int = T,
            alternative = 'greater'
)











