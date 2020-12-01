m <- matrix(c(11,12,13,14,21,22,23,24,31,32,33,34),nrow = 3,ncol = 4,byrow = TRUE)
m

m1 = m[-3,] # matrisin 3. satırını siler bunu kalıcı yapmak için atama yapmamız gerekir

m1 = m1[,-1] # matrisin 1. sütunun siler

m1

m[,-c(2,3)] # matristen 2. ve 3. sütunları çıkartır, kalıcı yapmak için atama yapmamız lazım


m[-c(2,3),-c(3,4)] # 2 ile 3. satırları ve 3 ile 4. sütunları sil


mcopy = m

mcopy[c(1,2),c(3)] = NA # matrisin 1 ile 2. satırının 3. sütununu NA olarak set et
mcopy

mcopy[1:3,c(1,2)] = mcopy[1:3,c(1,2)] * 5 # 1'den 3'e kadar (dahil) olan satırlar ve 1 ile 2. sütunları kendilerinin 5 katı ile güncelle
mcopy
