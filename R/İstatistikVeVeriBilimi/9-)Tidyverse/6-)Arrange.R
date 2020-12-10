# arrange fonksiyonu veriyi sıralamamızı sağlar


iris %>% arrange(Sepal.Length) # küçükten büyüğe doğru data frame'i Sepal.Length'e göre sıralar


iris %>% arrange(Sepal.Length, Sepal.Width) # önce Sepal.Length'e sonra Sepal.Width'e göre küçükten büyüğe sırala


iris %>% arrange(Sepal.Length,)


iris %>% arrange(desc(Sepal.Length)) # Sepal.Length'e göre büyükten küçüğe sıralar


arrange(iris,Sepal.Length) # istersek pipeline kullanmadan da kullanabiliriz


arrange(iris,desc(Sepal.Length),Sepal.Width) # sepal.length'e göre büyükten küçüğe, sepal.width'e göre küçükten büyüğe


