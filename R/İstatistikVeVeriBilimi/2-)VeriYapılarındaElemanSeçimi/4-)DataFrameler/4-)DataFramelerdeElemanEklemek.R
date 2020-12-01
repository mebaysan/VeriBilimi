df <- data.frame('A'=c(1:4),
                 'B' = c('A','B','C','D'),
                 'C'=seq(11,44,by=11))

df


df <- cbind(df, 'D'=seq(12,45,by=11)) # column bind -> sütun ekler. fonksiyondur, atamamız gerekir


df$Yeni <- c('E','K','L','E') # bu şekilde data frame değişken ekleyebiliriz
df

df['Yeni2'] <- c('E','L','K','E') # Yeni2 adında bir sütun eklenir
df

df[5,] <- c(1,2,3,4,5,6) # 5. satıra ekledim
df

df <- rbind(df,c(10:15)) # row bind -> satır ekler, sütun sayısı kadar ekler
df


cbind(df,data.frame('Eklenen1'=c(1:6),'Eklenen2'=c(1:6))) # data frame tipinde ekleyebiliriz
