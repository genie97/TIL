## R Language UNIT06

```R
# Install randomForest package
install.packages("randomForest")
library(randomForest)

# Build random forest model
SteventsForest = randomForest(Reverse~Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst, data = Train, ntree=200, nodesize=25)

# warning in CART, we added the argument method="class",
# so that it was clear that we're doing a classification problem
# The randomForest function does not have a method argument
# So when we want to do a classiication problem,
# we need to make sure outcome is a factor

# Convert outcome to factor
Train$Reverse = as.factor(Train$Reverse)
Test$Reverse = as.factor(Test$Reverse)

# Try agin
SteventsForest = randomForest(Reverse~Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst, data = Train, ntree=200, nodesize=25)

# Make predictions
PredictForest = predict(SteventsForest, newdata = Test)
table(Test$Reverse, PredictForest)

# Accuracy = 67%
# Accuracy Logistic Reg = 66.5%
# Accuracy CART = 65.9%
(40+74) / (40+37+19+74)

# Install cross-validation packages
install.packages("caret")
library(caret)
install.packages("e1071")
library(e1071)

# Define cross-validation experiment
# number = # of folds 10 here
numFolds = trainControl( method = "cv", number = 10 )

# Possible values for CP(Complexity paramter) parameter
cpGrid = expand.grid( .cp = seq(0.01,0.5,0.01))


# Perform the cross validation
# method = "rpart -> cross validate a CART model
train(Reverse ~ Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst, data = Train, method = "rpart", trControl = numFolds, tuneGrid = cpGrid )

# get a table describing the cross validation accuracy for differenct cp prameters
# First Column -> CP paramter that was tested
# Second Column gives the cross validation accuracy for that cp value
# The accuracy starts lower, and then increases, and then will start decreasing again
# Towards the end of the table it shows which CP value to use

# Create a new CART model with the CP value suggested by above model
# method = 'class' -> building classification tree
StevensTreeCV = rpart(Reverse ~ Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst, data = Train, method="class", cp = 0.18)

prp(StevensTreeCV)

# Make predictions
PredictCV = predict(StevensTreeCV, newdata = Test, type = "class")

# Confusion Matrix
# table(true outcome, prediction)
table(Test$Reverse, PredictCV)

#Accuracy = 0.724
#Accuracy of previous cart model = 0.659
(59+64) / (59+18+29+64)

# By using Cross Validation we are selecting a SMART parameter values

PredictROC = predict(StevensTreeCV, newdata = Test)
PredictROC

pred = prediction(PredictROC[,2], Test$Reverse)
perf = performance(pred, "tpr", "fpr")
plot(perf)
```

