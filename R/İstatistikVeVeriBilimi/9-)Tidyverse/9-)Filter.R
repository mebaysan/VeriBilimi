# filter fonksiyonu sayesinde veri setlerimizde filtreleme yapabiliriz

filter(iris, Sepal.Width < 3 & Species == 'setosa') # Sepal.Width  < 3 VE Species = setosa olanları getir


filter(iris, Sepal.Width < 3 | Species == 'setosa') # Sepal.Width < 3 VEYA Species = setosa olanları getir



iris %>% filter(Sepal.Length < 5 & Sepal.Width > 3) %>% # filtre uyguladık
  select(Sepal.Length,Sepal.Width,Species) %>% # istediğimiz değişkenleri seçtik
  group_by(Species) %>% # değişkene göre grupladık
  summarise( # özet tablo çıkartıyoruz
    Sepal.Length.Ortalaması=mean(Sepal.Length),
    Sepal.Width.Ortalaması=mean(Sepal.Width),
  )
