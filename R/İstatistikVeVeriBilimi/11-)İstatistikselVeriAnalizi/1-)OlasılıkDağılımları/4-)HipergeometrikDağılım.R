# Sonlu bir ana kütleden yerine konmadan yapılan (iadesiz) seçimlerde n seçimdeki başarılı olma olasılığı ile ilgilenen kesikli olasılık dağılımıdır.
# Binom dağılımı ile hipergeometrik dağılımı birbirinden ayıran en önemli nokta; binom dağılımı iadeli seçim yaparken hipergeometrik dağılım iadesiz seçim yapar

# N -> popülasyon büyüklüğü
# n -> yapılacak seçim sayısı
# D -> deneylerdeki toplam başarılı olma sayısı
# x -> seçimler sonrası elde edilen başarılı seçimler

# p(x) = choose(m, x) choose(n, k-x) / choose(m+n, k)
# x -> deney sonrası elde etmek istediğimiz olayların olasılığı
# m -> toplam başarılı durumlar sayısı
# n -> başarılı olma dışında kalan sayılar
# k -> kaç deneme yapacağız

?dhyper


dhyper(x = 4, m = 26, n = 26, k = 10) # 10 deneyde 52 kart içerisindeki 26 kırmızı karttan 4 tane kırmızı kart seçme olasılığı
# Bu örnek bir iskambil destesi içindir
## x -> 4 adet kırmızı kart elde etmek istiyoruz
## m -> toplamda 26 adet kırmızı kart vardır bu destede
## n -> popülasyon - m yani kırmızı kartlar dışında destedeki siyah kartlar
## k -> deney sayısı


dhyper(x = 1, m = 26, n = 26, k = 10) # 10 deneyde 52 kart içerisindeki 26 kırmızı karttan 1 tane kırmızı kart seçme olasılığı
dhyper(x = 12, m = 26, n = 26, k = 10) # 10 deneyde 52 kart içerisindeki 26 kırmızı karttan 12 tane kırmızı kart seçme olasılığı


plot(1:52,dhyper(1:52,m=26, n = 26, k = 10),
     pch=19,bty='L',
     col='orange')



phyper(q=5,m=26,n=26,k=10,lower.tail = T) # 10 deneyde 52 kart içerisindeki 26 kırmızı karttan 5 ve 5'ten daha az kırmızı kart çekme olasılığı
phyper(q=5,m=26,n=26,k=10,lower.tail = F) # 10 deneyde 52 kart içerisindeki 26 kırmızı karttan 5'ten daha fazla kırmızı kart çekme olasılığı



# Instagram'da reklam verilecek. Reklam sadece Üsküdar'da oturan
# erkek ve 20 - 25 yaş arasındaki kullanıcılara gösterilecek.
# Bu kritere uyan toplam 10000 kişinin instagram'da bulunduğu bilgisi var.
# 10000 kişinin 5000'i google arama verilerine göre yeni sezon kıyafetlere 
# ihtiyacı olacağı beklenmektedir. Anlaşmaya göre reklam 10000 kişi içerisinde
# 3000 kişiye yalnızca 1 kere gösterilecektir. Bu durumda reklamın kıyafet
# ihtiyacı olan en az 1500 kişiye gösterilme olasılığı nedir?

phyper(q=1500,m=5000,n=5000,k=3000, lower.tail = F)



# Olasılık değerine göre elde edilebilecek durum sayısı
qhyper(p=0.6, m = 5000, n = 5000, k = 3000, lower.tail = T) # %60 olasılıkla; 10000 kişilik hedef kitleden 3000'ine reklam göstersen kıyafet ihtiyacı olan 5000 kişiden bu kadarından az kişi reklam görür
qhyper(p=0.6, m = 5000, n = 5000, k = 3000, lower.tail = F) # %60 olasılıkla; 10000 kişilik hedef kitleden 3000'ine reklam göstersen kıyafet ihtiyacı olan 5000 kişiden bu kadarından fazlası reklam görür



# rastgele hipergeometrik dağılan veriler
rhyper(nn=50,m = 26,n=26,k=10) # 52 kartlık destede 10 seçim yapınca bulunan 26 kırmızı karttan elde edilebilecek kırmızı kart sayısı




# Soru:
## bir iş için başvuran adayların dördü erkek altısı kadındır. x işe alınan kadın
## sayısı olduğuna göre, işe üç kişi alındığında hiç kadın alınmaması olasılığını
# hesaplayınız
dhyper(x = 0, m=6,n=4,k=3)


# Soru:
## 1000 seçmenden 800 tanesi B partisine oy vermeyi düşünmektedir. Eğer seçmenler
## arasından rassal ve iadesi olarak 20 seçmen seçersek, bunlardan 14 tanesinin 
## B partisi taraftarı olma olasılığı nedir?
dhyper(x=14, m=800,n=200,k=20)









































































