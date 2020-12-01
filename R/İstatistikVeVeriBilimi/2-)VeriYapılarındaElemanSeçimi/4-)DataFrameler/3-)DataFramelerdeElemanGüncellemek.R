df <- data.frame('A'=c(1:4),'B'=c(5:8))
df

df[1,'B'] = 'Değişti' # 1. satır B sütununu değiştirir

df['A'] = 'DEGER' # tüm sütunu değiştirir
df

df[c(3,4),'A'] = c('Değişen1','Değişen2') # 3 ve 4. satırlardaki A sütununu değiştir
df
