install.packages('tidyverse') # paketi yüklememiz gerek

library('tidyverse') # paketi import ediyoruz


View(iris)

# select fonksiyonu sayesinde değişkenleri seçebiliriz

select(iris,Sepal.Length, Sepal.Width) # dpylr ile select fonksiyonu kullanarak değişken seçmek 

iris %>% select(Sepal.Length, Sepal.Width) # pipeline mantığı


