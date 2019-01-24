## R Language Project

Compare baseline  and linear regression model.

```R
# Get data pathe
getwd()

# Set data path
setwd("C:/Users/GENIE/Documents/R")

# Read data
data = read.csv("coinData.csv")
str(data)


data_star = data[c('name', 'Star', 'Market.Cap.billion.')]
colnames(data_star) = c("name", "star", "cap")
data_star[,2] = as.integer(gsub(",","",data_star[,2]))
data_star=data_star[complete.cases(data_star),]

# Sort data
sorted_data_star = data_star[order(-data_star$star),]
str(sorted_data_star)
sorted_data_star

# Load library
library(ggplot2)
ggplot(data=sorted_data_star, aes(x=star, y=cap)) + geom_point(aes(size=3, colour=sorted_data_star$name)) + geom_text(label=sorted_data_star$name) + geom_smooth()

cor(sorted_data_star$star, sorted_data_star$cap)
#Result: 0.9078217

# Remove index 1,2,7 of data 
s2 = sorted_data_star[c(1),c(2),c(7)]
s2 = sorted_data_star[-c(1,2,7),]

ggplot(data=s2, aes(x=star, y=cap)) + geom_point(aes(size=3, colour=s2$name)) + geom_text(label=s2$name) + geom_smooth()
cor(s2$star, s2$cap)
#Result: 0.1925724

s3 = sorted_data_star[sorted_data_star$cap < 100 & sorted_data_star$star <1000,]
ggplot(data=s3, aes(x=star, y=cap)) + geom_point(aes(size=3, colour=s3$name)) + geom_text(label=s3$name)
cor(s3$star, s3$cap)
#Result: 0.6813768

# Function convertNum
convertNum = function(i){
  bigdata[,i] = as.integer(gsub(",","",bigdata[,i]))
  }

# Make a data frame
bigdata = data[c('name', 'Root', 'Commit','Star', 'Contributor','Fork','Language', 'Market.Cap.billion.')]
colnames(bigdata) = c('name', 'root', 'commit','star', 'contributor','fork','language', 'market')

# Convert to integer
bigdata[,3] = as.integer(gsub(",","",bigdata[,3]))
bigdata[,4] = as.integer(gsub(",","",bigdata[,4]))
bigdata[,5] = as.integer(gsub(",","",bigdata[,5]))
bigdata[,6] = as.integer(gsub(",","",bigdata[,6]))

convertNum(3)
convertNum(4)
convertNum(5)
convertNum(6)

# baseline model
baseline = sum(bigdata$market) / nrow(bigdata)
baseline

# Linear regression model
model = lm(market~commit + star + contributor+fork, data=bigdata)
summary(model)

target = data.frame(commit = 9492, star = 106, contributor = 52, fork =29)
predict(model, newdata = target)
# 1 
# 201.2138 

target = bigdata
result = predict(model, newdata = target)
result = cbind(bigdata, result)
resultfinal = result[,c("name", "market", "result")]
resultfinal[,4] = resultfinal[,2] - resultfinal[,3]
colnames(resultfinal)[4] = "difference"
str(resultfinal)
resultfinal = resultfinal[order(resultfinal$difference),]
resultfinal

resultfinal$colour = ifelse(resultfinal$difference<0, "steelblue", "firebrick1")

resultfinal <- resultfinal[complete.cases(resultfinal),]
resultfinal

ggplot(resultfinal, aes(x=name, y=difference)) + geom_bar(stat="identity",fill=resultfinal$colour) + coord_flip()

coinTest = read.csv("coinData_test.csv")
colnames(coinTest) = c('name', 'root', 'commit','star', 'contributor','fork','language', 'market')
coinTest[,3] = as.integer(gsub(",","",coinTest[,3]))
coinTest[,4] = as.integer(gsub(",","",coinTest[,4]))
coinTest[,5] = as.integer(gsub(",","",coinTest[,5]))
coinTest[,6] = as.integer(gsub(",","",coinTest[,6]))

predictTest = predict(model, newdata=coinTest)
predictTest

SSE = sum(coinTest$market-predictTest)^2
SSE

SST = sum((coinTest$market-mean(bigdata$market))^2)
SST

R = 1-SSE/SST
R
```

