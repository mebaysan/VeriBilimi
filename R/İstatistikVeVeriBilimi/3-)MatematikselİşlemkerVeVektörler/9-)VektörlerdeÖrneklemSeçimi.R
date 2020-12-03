
x <- seq(10,100,by=10)

sample(x,replace=TRUE) # iadeli olarak örneklem çeker

sample(x,replace = FALSE) # iadesiz olarak örneklem çeker


sample(x,size = 3,replace = TRUE) # x vektöründen iadeli olarak 3 eleman seçer

set.seed(1) # rassallığı sabitliyoruz, içerisindeki parametre istediğimiz bir sayı olabilir
sample(x,size=2,replace=FALSE) # x vektöründen iadesiz olarak 2 örnek seç.
# set.seed(1) çalıştırıldığında seçilen örnekler aynı olur

