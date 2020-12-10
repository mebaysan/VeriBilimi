# slice fonksiyonu satır seçim işlemlerini gerçekleştirir

slice(iris,1,2) # 1. ve 2. satırları seçeriz


iris %>% select(Sepal.Length,Sepal.Width) %>% slice(1,2) # slice ve select pipeline ile kullanmak