## R Language UNIT3

```R
# Correlations
cor(wine$WinterRain, wine$Price)
cor(wine$Age, wine$FrancePop)
cor(wine)

# Read in test set
wineTest = read.csv("wine_test.csv")
str(wineTest)

# Make test set predictions
model4 = lm(Price~ AGST+HarvestRain+WinterRain+Age, data=wine)
predictTest = predict(model4, newdata=wineTest)
predictTest

# Compute R-squared
SSE = sum(wineTest$Price-predictTest)^2
SST = sum((wineTest$Price-mean(wine$Price))^2)
1-SSE/SST


```

