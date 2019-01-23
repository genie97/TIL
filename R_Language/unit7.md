## R Language UNIT07

```R
# Text Processig (Natural Language Processing)

# Read in the data
getwd()
setwd("C:/Users/GENIE/Documents/R")
tweets = read.csv("tweets.csv")
str(tweets)

# Install new packages
install.packages("tm")
library(tm)

install.packages("SnowballC")
library(SnowballC)

tweets$Negative <- as.factor(tweets$Avg <= -1)
table(tweets$Negative)

# Corpus: concept introduced by the tm pakage
# Corpus: collection of documents
# Convert the tweets to a corpus for pre-processing
# we will use tweets column of data frame using two functios corpus and VectorSource

# Create corpus
corpus = VCorpus(VectorSource(tweets$Tweet))

# Look at corpus
corpus
corpus[[1]]
corpus[[1]]$content

# Remove punctuation
corpus = tm_map(corpus, removePunctuation)
corpus[[1]]$content

# tm provides a list of stop words
# Look at stop words
stopwords("english")[1:10]

# We will remove all of these English stop words
corpus = tm_map(corpus, removeWords, c("apple", stopwords("english")))

# Stem document(remove words like ed, e etc)
corpus = tm_map(corpus, stemDocument)
corpus[[1]]$content

# investigate the corpus & prepare it for prediction problem
# DocumentTermMatrix: tm package provides a function that generates a matrix
# rows -> documents, in our case tweets
# columns -> words in those tweets
# The values in the matrix are the number of times that word appears in each documents

# Create matrix
frequencies = DocumentTermMatrix(corpus)
frequencies

# (documents/tweets: 1181, terms/words: 3289) after pre-processing

# Look at matrix
# inspect: to see the matrix
# inspect((frequencies(documents, words)))
inspect((frequencies[1000:1005, 505:515]))

# This data is sparse i.e. we have many zeros in our matrix
# Check for sparsity
# findFreqTerms: function to check most popular terms
# findFreqTerms(matrix lowfreq=minimum number of times a term must appear to be display
findFreqTerms(frequencies, lowfreq = 20)

# only 56 words appear at least 20 times in the tweets
# this means we have a lot of term that will be pretty useless for our prediction model
# The number of terms is an issue for two main reasons.
# computational: More terms means more independent variables
# which usually means it takes longer to build our model
sparse = removeSparseTerms(frequencies, 0.995)
sparse

# only has 309 words = 9% of the previous count of 3289 words
# Convert matrix to a data frame to use for the predictive model
# Make all variable names R-friendly
tweetsSparse= as.data.frame(as.matrix(sparse))
colnames(tweetsSparse) = make.names(colnames(tweetsSparse))


# Add dependent variable
tweetsSparse$Negative = tweets$Negative

library(caTools)
set.seed(123)

split = sample.split(tweetsSparse$Negative, SplitRatio = 0.7)
trainSparse = subset(tweetsSparse, split==TRUE)
testSparse = subset(tweetsSparse, split==FALSE)

library(rpart)
library(rpart.plot)

tweetCART = rpart(Negative~., data = trainSparse, method="class")
prp(tweetCART)

# Evaluate the performance of the model by making predictions
predictCART = predict(tweetCART, newdata = testSparse, type="class")

# Confusion Matrix using table function
# table(actual outcome, predictions)
table(testSparse$Negative, predictCART)
predictCART

# Compute accuracy
(294+18) / (294+6+37+18) 
# 결과값: 0.8788732

#Baseline accuracy: always predicts non negative
300 / (300+55)
# 결과값: 0.8450704

# CART model does better than simple baseline model
# Random forest model
library("randomForest")

set.seed(123)
tweetRF = randomForest(Negative~., data=trainSparse)

# Compute the Out-of-Sample predictions
predictRF = predict(tweetRF, newdata = testSparse)
```

