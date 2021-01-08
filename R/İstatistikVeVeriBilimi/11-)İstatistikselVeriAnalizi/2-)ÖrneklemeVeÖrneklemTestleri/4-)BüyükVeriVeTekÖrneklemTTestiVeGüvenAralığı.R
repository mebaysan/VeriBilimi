# Dataset: https://www.kaggle.com/spscientist/students-performance-in-exams

df <- read.csv('StudentsPerformance.csv')
nrow(df)

hist(df$math.score)

mean(df$math.score)


sample1 <- sample(df$math.score,size=50)
t.test(sample1,mu=70,alternative = 'two.sided',conf.level = 0.95)

sample2 <- sample(df$math.score,size=50)
t.test(sample2,mu=70,alternative = 'two.sided',conf.level = 0.95)


result <- character(50)
for (i in 1:50) { # 50 kere t testi yaptık
  ornek <- sample(df$math.score,50)
  sonuc <- t.test(ornek,mu=70)
  p <- sonuc$p.value
  if(p >= 0.05){
    result[i] <- 'KABUL'
  }else{
    result[i] <- 'RED'
  }
}
table(result) # veri sayısı çok olduğunda bu şekilde sample'lar alarak t testlerini uygulamamız gerekir

