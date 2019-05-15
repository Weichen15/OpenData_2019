gp <- read.csv(file.choose(), header=TRUE)
print(gp)
summary(gp)
gp.scale <- scale(gp[,1:5], center = TRUE, scale = TRUE)
gp.scale.DataFrame <- data.frame(gp.scale)
gp.scale.DataFrame.lm <- lm(daily_mean_v ~ bear + bull + comment + count , data = gp.scale.DataFrame)
gp.scale.DataFrame.lm
summary(gp.scale.DataFrame.lm)




