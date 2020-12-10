df <- read.csv('CSV__singapore.csv')
View(df)
# vektörlerde tip dönüşümü yaptığımız gibi burda da tip dönüşümü yaparız
names(df)

class(df$name)

class(df$id)

as.factor(as.character(df$id)) 


