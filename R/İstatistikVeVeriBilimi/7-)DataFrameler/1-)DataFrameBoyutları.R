df <- data.frame('A'=c(12,13,14,15),'B'=c(2,3,4,5),'C'=c('A','B','C','D'))
df

length(df$A) # df'in A değişkeni'nin (sütunu) eleman sayısı

nrow(df) # df'in kaç satırı var

ncol(df) # df'in kaç sütunu var


length(df) # length fonksiyonu dataframe'de sütunları sayar


dim(df) # dimention -> satır x sütun olarak bize gösterir

dim(df)[[1]] # df'İn satır sayısı
dim(df)[[2]] # df'İn sütun sayısı

