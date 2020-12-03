x <- c(1:10)

sqrt(x) > 2 # bu tarz LOGICAL bir sorgu bize indisleri verir
x > 6 # logical
x < 3 # logical

x[x>6]  # x'in 6'dan büyük elemanları

x[x<3] # x'in 3'ten küçük elemanlarını getirir

x[(x**2)>25] # karesi 25'ten büyük olan değerleri getirir

x[sqrt(x) < 2] # karekökü 2'den küçük olan değerleri getirir



