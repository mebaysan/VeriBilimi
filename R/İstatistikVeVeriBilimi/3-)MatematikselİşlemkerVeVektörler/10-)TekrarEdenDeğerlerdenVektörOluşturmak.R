rep(4,5) # repeat (rep) fonksiyonu: 5 kere 4'ü tekrar et


x <- c(rep('A',4),rep('B',3),rep('Y',7)) # 4 tane A, 3 tane B ve 7 tane Y'den oluşan vektör
x

rep(c(1,2,3,4,5),5) # 5 kere tekrar eden bir vektör

rep(c(1,2,3),each=2) # içerideki vektörü her biri 2 kere olacak şekilde tekrar et


rep(c(1,2,3),each=2,times=3) # içerideki vektörü her biri 2 kere olacak şekilde 3 kere tekrar et
