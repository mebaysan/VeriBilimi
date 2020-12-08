x <- c(12,13,14)
y <- c('A','B','C')
z <- c(T,F,T)
f <- factor(c('F1','F2','F3'))



is.numeric(x) # bu vektör numeric mi
is.integer(x) # integer olarak kabul etmiyor, bunun sebebi ise R default olarak numeric olarak almakta
is.character(y) # karakter mi
is.factor(f) # factor mu
is.logical(z) # logical mi
