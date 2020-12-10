library('readxl')
islem_df <- read_excel('Transactions.xlsx')
demografik_df <- read_excel('Demografik.xlsx')

# merge işlemini join olarak düşünebiliriz

birlesmis <- merge(islem_df,demografik_df,by.x='CUSTOMER_ID',by.y='ID')
# ilk parametre x, ikinci parametre y
# by.x -> x df'inde hangi değişken
# by.y -> y df'inde hangi değişken
# eğer iki df'de de aynı key'ler üzerinde merge edeceksek by parametresini vermemiz yeter
View(birlesmis)
