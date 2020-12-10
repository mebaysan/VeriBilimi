library(readxl) # excel okumak için kütüphane
df <- read_excel('6.1-)singapore.xlsx') # excel dosyasının yolu
View(df) # okuduğun df'i göster


names(df)

write.csv(df,file = '6.2-)singapore.csv') # df'i csv olarak yaz



#setwd('PATH') # çalışma dizinimi set eder

getwd() # çalışma dizinimin pathini verir

list.files() # çalışma dizinindeki dosyaları listeler


df <- read.csv('6.2-)singapore.csv',sep = ',',header = T,dec = '.')
# çalışma dizinine yazar csv'i
# sep -> veriler neyle ayrılmış
# header -> ilk satırda değişken isimleri var mı
# dec -> ondalıklı sayılar ne ile ayrılmış

View(df)
