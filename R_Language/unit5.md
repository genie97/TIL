## R Language UNIT5

> 1. Receiver Operator Characteristic (ROC) Curve
>
> - ROC 그래프는 가로축을 FP Rate(Specificity) 값의 비율로 하고 세로축을 TP Rate(Sensitivity)로 하여 시각화 한 것이다.
>
> - 그래프가 위로 갈 수록 좋은 모델이고, 적어도 Y=x 그래프보다 위에 있어야 
>
>   어느정도 쓸모 있는 모델로 볼 수 있다.
>
>
> 2. High threshold
>
> - High specificity (poor care라고 예측한 것이 맞을 확률이 낮다)
> - Low sensitivity
>
>
>
> 3. Low threshold
>
> - Low specificity (Poor case라고 예측한 것이 맞을 확률이 높다)
> - High sensitivity
>
>
>
> 4. Choose best threshold for best trade off
>
> - cost of failing to detect positives (positive를 감지하지 못하는 비용)
> - cost of rasing false alarms (false 발생의 증가 비용)
>
> - **이 두가지를 잘 고려해서 best threshold를 선택해야 한다**

------

> ROC는 그래프이기 때문에, 모델의 정확도를 하나의 숫자로 나타내기 어렵다 => AUC 사용
>
> AUC값은 ROC 그래프의 면적이 된다 (MAXIMUM = 1)

------

> 1. accuracy(ACC) = (TP + TN) / (TP + TN + FP + FN)
>
> - 모델이 얼마나 정확하게 분류를 하는지를 나타냄
>
> 2. error rate(ERR) = (FP + FN) / (TP + TN + FP + FN)
>
> - 전체 데이터 중에서 잘못 분류한 비율을 나타냄
>
> 3. sensitivity(TPR/Recall) = TP / (TP + FN)
>
> - 모델이 얼마나 정확하게 Positive 값을 찾느냐를 나타냄
>
> 4. precision(PREC) = TP / (TP + FP)
>
> - positive로 예측한 내용 중에, 실제 positive의 비율
>
> 5. specificity(TNR) = TN / (TN + FP)
>
> - negative로 판단한 것 중에, 실제 negative의 비율
>
> 6. False Positive Rate(FPR) = FP / (FP + TN)
>
> - 원래는 positive 값이지만, negative로 잘못 판단한 비율

```R
# Install and load ROCR package
install.packages("ROCR")
library(ROCR)

# Prediction function
ROCRpred = prediction(predictTrain, qualityTrain$PoorCare)

# Performance function
ROCRperf = performance(ROCRpred, "tpr", "fpr")

#Plot ROC curve
plot(ROCRperf)

# Add colors
plot(ROCRperf, colorize = TRUE)

# Add threshold (0~1사이에서 0.1씩 증가)
# text.adj(x,y): plot에 text를 추가하는 함수
plot(ROCRperf, colorize=TRUE, print.cutoffs.at=seq(0,1,by=0.1), text.adj=c(-0.2,1.7))

# Read in the data
stevens = read.csv("stevens.csv")
str(stevens)

# Split the data
library(caTools)
set.seed(3000)
spl = sample.split(stevens$Reverse, SplitRatio = 0.7)
Train = subset(stevens, spl == TRUE)
Test = subset(stevens, spl==FALSE)

# Fit Logistic Regression model
logRegr = glm(Reverse~., data = Train, family = binomial)
summary(logRegr)

# Install rpart library
install.packages("rpart")
library(rpart)
install.packages("rpart.plot")
library(rpart.plot)

# CART model
StevensTree = rpart(Reverse ~ Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst, data = Train, method="class", minbucket=25)
# method = "class(classification)" --> rpart to build a classification tree
# instead of a regression tree
# minbucket: limits the tree so that it does not overfit to our training set
# : 25 difference num of subset from train data
prp(StevensTree) # plot tree

# Make predictions
# type = "class" --> this argument required when making predictions
# for the CART model if want the majority class predictions
predictCART = predict(StevensTree, newdata = Test, type="class")

# Confusion Matrix
# Table(True outcome value, predictions)
tabLe(Test$Reverse, predictCART)

# 결과 값
# Accuracy CART = (41 + 71) / (41 + 26 + 22 + 71) = 0.65

# ROC curve
library(ROCR)

# Compute predictions without the type = "Class"
PredictRoc = predict(StevensTree, newdata=Test)
PredictRoc #Gives two number probability of outcome 0 and 1
# These numbers give the percentage of training set data in that subset with outcome 0
# and the percentage of data in the training set in that subset with outcome 1

# Using second column to compute the ROC curve
pred = prediction(PredictRoc[,2], Test$Reverse)
perf = performance(pred, "tpr", "fpr")
plot(perf)
```

