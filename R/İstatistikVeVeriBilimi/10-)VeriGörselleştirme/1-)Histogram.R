# histogram grafiği bize verilerin dağılımı hakkında bilgi verir

hist(iris$Sepal.Length) # bir vektörün histogramı
# x ekseni değerleri gösterirken
# y ekseni frekansları gösterir


hist(iris$Sepal.Length, main='Histogram Grafiği')
# histogram'ın başlığını değiştirmek istersek main parametresini vermemiz gerekmektedir


hist(iris$Sepal.Length, main='Histogram Grafiği',
     xlab='x ekseni', # x ekseninin başlığını değiştirir
     ylab='y ekseni') # y ekseninin başlığını değiştirir


hist(iris$Sepal.Length,breaks=30) 
# breaks parametresi sütunların kırılımını gösterir



hist(iris$Sepal.Length, xlim = c(0,10)) # xlim parametresi ile x eksenine limitler belirleyebiliriz


hist(iris$Sepal.Length, ylim = c(0,30)) # ylim sayesinde y eksenine limit uygularız


hist(
  iris$Sepal.Length,
  col = '#8e44ad', # barların rengini değiştirir, renk kodu yazabiliriz
     )


hist(
  iris$Sepal.Length,
  col = c('pink','yellow','purple') # birden fazla renk verirsek sırasıyla renkleri dizer
)



hist(
  iris$Sepal.Length,
  breaks=30,
  col = c('pink','yellow','purple','orange')
)





hist(
  iris$Sepal.Length,
  main='Yoğunluk Eğrisi',
  xlab = 'Değerler',
  ylab='Yoğunluk',
  prob = T,
  col='orange',
)
lines(density(iris$Sepal.Length, adjust=2), col='red',lwd=3, lty='dotted') 
# önce histogramı çizdik sonrasında lines ile yoğunluk eğrisini çizdirdik
# adjust parametresi eğrideki kıvrımları sadeleştirir
# col çizgiye renk verir
# lwd ise çizginin kalınlığını ayarlar
# lty çizginin tipini belirler





