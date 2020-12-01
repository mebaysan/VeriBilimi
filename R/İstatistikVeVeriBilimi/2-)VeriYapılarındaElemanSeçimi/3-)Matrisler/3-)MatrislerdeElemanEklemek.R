m <- matrix(c(11,12,13,14,21,22,23,24,31,32,33,34),nrow = 3,ncol = 4,byrow = TRUE)
m

m <- cbind(m,c(15,25,35)) # yeni bir sütun ekler. ilk parametre hangi matrise, 2. parametre ise sütun vektörü
# column bind -> satır sayısı kadar elemanlı vektör alır



m <- rbind(m,c(41,42,43,44,45))
# row bind -> sütun sayısı kadar elemanlı vektör alır
m

