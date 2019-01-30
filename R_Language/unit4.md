## R Language UNIT4

```R
# 로지스틱 회귀분석
# 선형 회귀분석과 달리 결과변수(종속변수)가 범주형 데이터인 경우 사용한다
# 0 혹은 1 로 판별 가능한 경우에는 로지스틱 회귀분석을 이용한다

# Read in dataset
quality = read.csv("quality.csv")

# Look at structure
str(quality)

# Table outcome to see how many people received good care and how many poor care
# 0 = Good Care
# 1 = Poor Care
table(quality$PoorCare)

# First build a simple baseline model
# Most frequest outcome = baseline model for classification problem
# Simple Baseline accuracy
98 / 131

# Install and load caTools package
install.packages("caTools")

# Load the package
library(caTools)

# Randomly split data
# 시드값은 컴퓨터 내부에서 돌아가는 특정한 난수 생성을 처음 시작값
# 매번 같은 값이 나오게 만든다
# 랜덤한 시드값 설정: 난수를 설정해주는 함수
set.seed(88) #So, that all of us get the same split 

# 75% of data = Training Set to build the model
# 25% of data = Test Set to test the model
# Sample.split = 
split = sample.split(quality$PoorCare, SplitRatio = 0.75)

# True = Put the observation in training set 
# False = Put the observaton in test set
# Ratio값으로 test set과 training set으로 나눈다
# 여기서는 SplitRatio가 0.75이므로 training set : test set = 3 : 1 

# Look at the Split
split

#Creating training and testing sets
qualityTrain = subset(quality, split==TRUE)
qualityTest = subset(quality, split==FALSE)

#Look at number of rows in training and test set
nrow(qualityTrain)
nrow(qualityTest)

# Logistic Regression Model with 2 independent variables
# Family = binomial -> tells to build to a logistic reg model
# GLM = Generalized Linear Model
QualityLog = glm(PoorCare ~ OfficeVisits+Narcotics, family=binomial, data=qualityTrain)
summary(QualityLog)

# Make predictions on training set
# Type = reseponse -> tells the predict function to give probabilities
predictTrain = predict(QualityLog, type="response")

# Analyze predictions
# Since probabilities, therefore, all number bet 0 and 1
summary(predictTrain)

# The outcome of a logistic regression model is a probability -> threshold value
# If P(PoorCare = 1) >= t: predict poor quality
# If P(PoorCare = 1) < t: predict good quality

# A model with a higher threshold will have a lower sensitivity and a higher specificity
# A model with a lower threshold will have a higher sensitivity and a lower specificity

# If we're predicting higher probabilities for the actual poor care cases as we expect 
# average predition for each of the true outcome
tapply(predictTrain, qualityTrain$PoorCare, mean)

# 결과에 대한 설명
# all of the true poor care cases, we predict an average probabilities of about 0.44
# all of the true good care cases, we predict an average probabilities of about 0.19

# Confusion matrix for threshold of 0.5
# First argument = what we want to label the rows by, should be the true outcome, which is qualityTrain$PoorCare
# Second argument = what we want to label the columns by, will be predictTrain, or our predictions, greater than 0.5. 
table(qualityTrain$PoorCare, predictTrain > 0.5)

# TP: True Positive
# TN: True Negative
# FP: False Positive
# FN: False Negative
# Sensitivity (TPR) = TP/P = TP / TP + FN
# Specificity (TNR) = TN/N = TN / TN + FP

# Sensitivity and specificity
10/(15 + 10)
70/(70 + 4)

#Confusion matrix for threshold of 0.7
table(qualityTrain$PoorCare, predictTrain > 0.7)

# Sensitivity and specificity
8/25
73/74

#Confusion matrix for threshold of 0.2
table(qualityTrain$PoorCare, predictTrain > 0.2)

# Sensitivity and specificity
16/25
54/74
```

