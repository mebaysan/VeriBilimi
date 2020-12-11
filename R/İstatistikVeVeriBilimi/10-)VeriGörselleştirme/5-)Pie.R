table_ <- table(mtcars$gear)

prop_ <- prop.table(table_)

labels = character()

for (v in names(table(mtcars$gear))) {
    label <- paste(v,'vitesli')
    labels <- append(labels,label)
}




pie(prop_,
    main='Pasta Grafiği',
    labels=labels,
    col=c('orange','pink','cyan'),
    init.angle = 180, # 180 derece döndürür
    border='red', # kenar çizgilerini renklendirir
    lty=2, # kenar çizgisini noktalaştırır
    radius = 1.1 # grafiği büyütür
    )

