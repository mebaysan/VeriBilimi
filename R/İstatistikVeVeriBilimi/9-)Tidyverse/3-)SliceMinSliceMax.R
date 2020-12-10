# slice_min ve slice_max fonksiyonları parametre olarak 
# verdiğimiz değişkendeki parametre sayısı kadar minimum ve max değerleri alır


iris %>% slice_min(order_by = Sepal.Length,n=10) # 10 tane minimum değer

iris %>% slice_max(order_by = Sepal.Length,n=10) # 10 tane maximum değer




iris %>% select(Sepal.Length,Sepal.Width) %>% slice(1:10) %>% slice_max(order_by=Sepal.Length,n=2)