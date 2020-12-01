df <- data.frame('A' = c(1,2,3,4,5),
                 'B' = c('A','B','C','D','E'))

df[1,1] # matrislerdeki gibi satır-sütun olarak seçebiliriz
df[1,]
df[,1]


df[,c(1,2)] # tüm satırlar ile 1 ve 2. sütunları seç
df[1:2,] # 1'den başla 2. satıra kadar ve tüm sütunları seç


df['A'] # dataframe'in A sütunu (data frame olarak döner)


df[['A']] # data frame'in A sütunu (vektör olarak döner)


df$A # vektör olarak A sütununu seçer

df[c('A','B')] # A ve B sütunlarını seçer

