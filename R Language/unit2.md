## R Language UNIT2

```R
#Reading csv file
WHO = read.csv("WHO.csv")
setwd("C:\Users\GENIE\Documents\R")
setwd("C:\\Users\\GENIE\\Documents\\R")
WHO = read.csv("WHO.csv")
summary(WHO)

#Subsetting
WHO_Europe = subset(WHO, Region=="Europe")
str(WHO_Europe)

#Writing csv file
write.csv(WHO_Europe, "WHO_Europe.csv")
getwd()

# basic data analysis
WHO$Under15

# Percentage of population Under 15
mean(WHO$Under15)

# SD of percentage of population Under 15
sd(WHO$Under15)

# Statical Summary of just one variable
summary(WHO$Under15)

# min value
min(WHO$Under15)

# which.max()/min() -> max, min에 대한 index값이 반환된다.
which.min(WHO$Under15)
WHO$Country[86] 
which.max(WHO$Under15)

# WHO$Column명[index] -> 해당 column의 index값이 반환된다.
WHO$Country[124]

# Scatter plot
plot(WHO$GNI, WHO$FertilityRate)

# Subsetting
Outliers = subset(WHO, GNI>10000 & FertilityRate>2.5)

# nrow() 해당 data frame에 대한 row개수가 반환된다.
nrow(Outliers) 
Outliers[c("Country", "GNI", "FertilityRate")]
 
# histogram
hist(WHO$CellularSubscribers)

# Boxplot
boxplot(WHO$LifeExpectancy~WHO$Region)

# 박스 안에 진한 선이 median
# 박스의 첫번째 선이 1st Quartile
# 박스의 끝 선이 3st Quartile
# 맨 밑에 있는 선이 minimum
# 맨 위에 있는 선이 maximum
# 동그라미가 Outlier
# min~max를 whiskers라고 한다
# whiskers는 Inter Quarter Range * 1.5로 지정하는 것이 보통이다.
# outlier는 whiskers 를 벗어난 값이라고 할 수 있다.
# 1st~3st가 중간에서의 50% 범위내에 있는 값들 => 박스형태로 나타남

# tapply splits data by second argument and applies
# third argument function to variable
# given as the first argument
# tapply(a,b,function)
# b에 대한 function(a)의 결과값을 반환 
tapply(WHO$Under15, WHO$Region, min)
tapply(WHO$LitracyRate, WHO$Region, min)
tapply(WHO$LiteracyRate, WHO$Region, min, na.rm=TRUE)




# Linear Regression
# Variable independent/dependent (독립/종속변수)
# Building baseline model
# Baseline model: 데이터 y값에 대한 평균값
# Predict dependent value
# Linear Regression Model

# R Language Rinear Regression
# One variable
model1 = lm(Price~AGST, data = wine)
summary(model1)
# SSE: 오류^2에 대한 합
# SST: (Y-Y의 평균)에 대한 합 
# 각 데이터들을 적절히 대표한다고 볼 수 있는 값
# SST = SSE + SSR
SSE = sum(model1$residuals^2)
SSE

#결과값에 대한 분석 및 설명
# significant: 각 변수들이 가지는 중요도라고 보면됨 
# ***: 모델에 영향을 많이 끼치는 변수
# Intercept: 절편
# single / multiple variable로 나누어짐
# Residual: 오류
# R = 1 - SSE/SST
```

