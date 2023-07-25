url = "http://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv"
mtcars<-read.csv(file = url,head=TRUE,sep = ",")
mtcars
head(mtcars)
tail(mtcars)
str(mtcars)
names(mtcars)
mtcars[1,]
mtcars[,2]
mtcars$cyl
mtcars[3,4]
mtcars[mtcars$cyl>4,]
mtcars[mtcars$cyl>4 & mtcars$gear>4,]
mtcars[mtcars$cyl>4 & mtcars$gear==4,]
mtcars[mtcars$cyl>4|mtcars$gear==4,]
mtcars[mtcars$cyl>4|mtcars$gear!=4,]
ncol(mtcars)
dim(mtcars)
str(mtcars)
mean(mtcars$hp,na.rm = TRUE)
median(mtcars$hp,na.rm = TRUE)
min(mtcars$hp,na.rm = TRUE)
max(mtcars$hp,na.rm = TRUE)
quantile(mtcars$hp,na.rm = TRUE)
var(mtcars$hp,na.rm = TRUE)
sd(mtcars$hp,na.rm = TRUE)
summary(mtcars$hp,na.rm = TRUE)
library("ggplot2")
png(file = "C:\\Users\\Chris\\projects\\Tomcat\\webapps\\lis4369/p2/qplot.png")
qplot(disp,mpg,data = mtcars,
 xlab= "Displacement",
 ylab= "MPG",
 colour=cyl,
  main = "Christopher Valverde:Displacement vs MPG")
dev.off()

png(file = "C:\\Users\\Chris\\projects\\Tomcat\\webapps\\lis4369/p2/qplot2.png")
plot(mtcars$wt,mtcars$mpg,
     main = "Christopher Valverde: Wieght vs MPG",
     xlab = "Weight in Thousands",
     ylab = "MPG",
     las= 1)
dev.off()

