
x <- c(1,2,3,4)

matrix(x,nrow = 2, ncol = 2)
# matrix fonksiyonu sayesinde matris oluşturabiliriz
# nrow -> kaç satır olacak
# ncol -> kaç sütun olacak

matrix(x,nrow = 2, ncol = 2, byrow = TRUE) # byrow = TRUE -> vektörü oluşturmaya satırlardan başlar


vektor <- c(1,2,3,4,5,6,7,8)

matrix(vektor, nrow=2, ncol=4)
matrix(vektor, nrow=4, ncol=2,byrow=TRUE)
