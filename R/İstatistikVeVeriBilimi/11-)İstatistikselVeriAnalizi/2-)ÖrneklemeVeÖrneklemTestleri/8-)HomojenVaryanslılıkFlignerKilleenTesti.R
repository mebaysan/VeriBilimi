# veriler kesikli olsa da kullanabiliriz
# normal dağılım yoksa daha iyi sonuçlar verir

View(warpbreaks)

shapiro.test(warpbreaks$breaks[warpbreaks$wool == 'A'])
shapiro.test(warpbreaks$breaks[warpbreaks$wool == 'B'])

boxplot(warpbreaks$breaks ~warpbreaks$wool)

# H0: varyanslar homojendir
# H1: varyanslar homojen değildir
# p-value > 0.05 ise H0 reddedilemez
fligner.test(warpbreaks$breaks~warpbreaks$wool)
