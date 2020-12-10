my_func <- function(){
  x <- as.numeric(readline(prompt = 'Hangi sayının üssünü almak istersiniz')) # readline olarak alınan değer CHARACTER'dir. Bu sebeple bunu numeriğe çeviriyoruz
  y <- readline(prompt = 'Üssü giriniz')
  y <- as.numeric(y)
  cat(x,'^',y,' = ',x**y)
}

my_func()
