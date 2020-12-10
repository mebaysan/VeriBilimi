# mutate fonksiyonu sayesinde tip dönüşümleri yapabiliriz

iris %>% mutate(Sepal.Length = log(Sepal.Length)) # sepal length'in logaritması alınmış




iris %>% mutate(Sepal.2Ussu = Sepal.Length**2)  # Sepal.Length'in 2 üssü alınmış hali olarak bir değişken ekledik


iris %>% mutate(Karakter = as.character(Species)) # karakter veri tipinde yeni bir değişken oluşturduk


iris %>% mutate_if(is.numeric, function(x){x * 10}) 
# koşullu olarak mutate işlemi gerçekleştirebiliriz, eğer değişkenler numeric se 10 ile çarp

