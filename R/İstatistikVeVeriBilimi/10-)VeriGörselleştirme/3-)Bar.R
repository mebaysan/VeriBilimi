# kategorik değişkenleri görselleştirmek istersek bar chart kullanırız
View(mtcars)


height <- table(mtcars$cyl)


barplot(height=height, # kontenjans tablosu alır
        names.arg = c('4 silindir','6 silindir','8 silindir'), # sırasıyla isimleri veririz
        col='orange', # bar rengi değiştirir
        border = 'orange' # kenar renklerini değiştirir
        )


barplot(height=height,
        horiz = T, # bar chartı yatırır
        names.arg = c('4 silindir','6 silindir','8 silindir'),
        cex.axis = 0.8, # eksen yazılarını boyutlandırır
        cex.names = 0.8 # bar isimlerini boyutlandırır
)



barplot(height=height, 
        names.arg = c('4 silindir','6 silindir','8 silindir'),
        col='orange',
        border = 'orange',
        axis.lty = 1 # alttaki çizgiyi stillendirir
)



grup_f <- function(x){
  cey <- quantile(x)
#  result <- character(length = length(x))
  result <- character() # character tipinde bir vektör oluşturuyoruz
  g1 <- which(x <= cey[2]) # %25'ten küçük olanlar
  g2 <- which(x <= cey[3] & x > cey[2]) # %50'ten küçük olanlar
  g3 <- which(x <= cey[4] & x > cey[3]) # %75'ten küçük olanlar
  g4 <- which(x <= cey[5] & x > cey[4]) # %100 olanlar
  
  
  result[g1] <- 'Grup 1'
  result[g2] <- 'Grup 2'
  result[g3] <- 'Grup 3'
  result[g4] <- 'Grup 4'
  
  return(result)
  
}

res <- grup_f(mtcars$mpg)

barplot(height = table(res), col='orange')


























































































