m <- matrix(c(11,12,13,14),nrow = 2,ncol = 2,byrow = TRUE)
m


m[1,1] # 1. satır 1. sütun

m[1,c(1,2)] # 1. satır, 1. ve 2. sütun

m[1,1:2] # 1. satır, 1. ve 2. sütun

m[1,] # 1. satırı komple al

m[,2] # 2. sütunu komple al
