View(mtcars)


table(mtcars$gear,mtcars$cyl)

h <- table(mtcars$gear,mtcars$cyl)


par(mar=c(5.1,5.1,5.1,5.1),xpd=T)
barplot(h,
        main='Stacked Bar Grafiği',
        xlab='Silindir',
        ylab='Frekans Değerleri',
        axis.lty=1,
        col=c('orange','purple','pink'),
        legend=c('3 vitesli','4 vitesli','5 vitesli'),
        args.legend=list( # legend argümanları
          bty='n', # legend'in border tipi
          horiz=T, # lejantı yatay yapar
          xjust=0.7,
          yjust=-0.7,
          cex=0.8
          )
        )


View(h)
