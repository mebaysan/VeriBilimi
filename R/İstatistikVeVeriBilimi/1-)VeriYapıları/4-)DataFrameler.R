x <- c(10,20,30,40)
y <- c('A','B','C','D')
z <- c(1,2,3,4)

df <- data.frame(x,y,z) # DataFrame oluşturmak için kullanılan fonksiyon
df

View(df) # RStudio'nun kendi DF gösterme formatını çalıştırırız

# DF oluştururken değişkenlerin eleman sayıları eşit olmalıdır!

df <- data.frame('X Değişkeni' = x, 'Y Değişkeni' = y, 'Z Değişkeni' = z) # DF oluştururken değişken isimlerini verebiliriz
View(df)


View(data.frame(
  'A' = c(1,2,3),
  'B' = c(4,5,6),
  'C' = c(7,8,9)
)) # değişkene atamadan bir DF oluşturduk

# değişken isimlerinin arasında boşluk varsa R otomatik olarak boşluk yerine '.' ekler
