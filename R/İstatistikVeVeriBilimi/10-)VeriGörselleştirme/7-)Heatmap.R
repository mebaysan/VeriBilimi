# sıcaklık haritası - heatmap
## veri setinin büyük değerlerden veya küçük değerlerden oluşması


# HEATMAP'ler MATRIS ALIRLAR
View(mtcars)

mtcars_matrix <- as.matrix(mtcars)
View(mtcars_matrix)


heatmap(mtcars_matrix,
        scale='column' # sütunlar bazında scale işlemi gerçekleştireceğiz dedik
        )


heatmap(mtcars_matrix,scale='column',
        Colv = NA,Rowv = NA # dendogramları deaktif eder
        ) 

install.packages('RColorBrewer')
library(RColorBrewer)

heatmap(mtcars_matrix,scale='column',
        Colv = NA,Rowv = NA,
        col=colorRampPalette(brewer.pal(9,'Blues'))(25), # Mavilerden oluşan renk paleti kullan
) 
legend(x='bottomright',legend=c('Min','Ort','Max'),
       fill = colorRampPalette(brewer.pal(9,'Blues'))(3) # legendi renklerde doldurur
       )
