df <- data.frame('A'=c(1:5),'B'=c(6:10),'C'=c(11:15))
df


df[-2] # 2. sütunu çıkartır


df[-c(1,4),-1] # 1'den 4'e kadar satırları ve 1.sütunu çıkar

df[3] = NULL # data frame'in 3. sütununu kaldırır


df <- data.frame('A'=c(1:5),'B'=c(6:10),'C'=c(11:15))

df[,-c(1,3)] # 1 ve 3. sütunlar gider (vektör döner)

df[-c(1,3)] # 1 ve 3. sütunlar gider (data frame döner)

df['D'] = c(1:5) # data frame'e D sütununu ekledik

df[c('A','D')] = NULL # A ve D sütunlarını kaldırdık
df

df[-1,] # 1. satırı kaldırır

df[-c(2:4),] # 2,3 ve 4. satırları çıkar
