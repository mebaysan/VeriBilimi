df <- read.csv('CSV__singapore.csv')

names(df)


attach(df) # data frame içerisindeki değişkenleri dışarı çıkartmamızı sağlar

host_name # attach fonksiyonu sayesinde artık bu değişken dışarı da çıkmış oldu bu sayede direkt olarak erişebiliyoruz

class(host_name)


detach(df) # dışarı çıkarttığımız değişkenleri yerine koyar diyebiliriz. Artık değişkenlere direkt olarak erişemeyiz

# UNUTMAMALIYIZ Kİ; NE KADAR ÇOK ATTACH YAPTIYSAK O KADAR DETACH ETMEMİZ GEREKİR!



with(df, print(host_name)) # ilk parametre veriyi alır, ikinci parametre de bu veri ile ne yapılacağıdır


with(df, 
     {
       x<- mean(price)
       y <- x - 5
       print(y)
     } # eğer birden fazla işlem yaptıracaksak bracket içerisinde yazmamız gerekir {}
    )
