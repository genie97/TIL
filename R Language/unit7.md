## R Language UNIT07

```R
# Text Processig (Natural Language Processing)

# Read in the data
getwd()
setwd("C:/Users/GENIE/Documents/R")

# Since working with text data here, extra argument stringsAsFactors=FALSE
# Avg= Average sentiment score
tweets = read.csv("tweets.csv")
str(tweets)

# Create dependent variable
# more interested to detect the tweets with clear negative sentiment,
# define a new variable in data set tweets called Negative.

tweets$Negative <- as.factor(tweets$Avg <= -1)
# This will set tweets$Negative equal to true if the average sentiment score <= -1 -> Negative sentiment
# set tweets$Negative equal to false if the average sentiment score > -1.

table(tweets$Negative)

# 182 of the 1,181 tweets, or about 15%, are negative.

# Pre-process the data to use Bag of Words
# Install new packages
install.packages("tm")
library(tm)

install.packages("SnowballC")
library(SnowballC)

# Corpus: concept introduced by the tm pakage
# Corpus: collection of documents
# Convert the tweets to a corpus for pre-processing
# we will use tweets column of data frame using two functios corpus and VectorSource

# Create corpus
corpus = VCorpus(VectorSource(tweets$Tweet))

# Look at corpus
corpus
corpus[[1]]

#check that the documents match the tweets
#Shows first tweet in corpus
corpus[[1]]$content

# Start pre-proceeing the data
# Stemming, removing stop words

# Convert to lower-case
# tm_map(name of our corpus, what we want to do)
corpus = tm_map(corpus, content_transformer(tolower))

corpus[[1]]$content

# Remove punctuation
corpus = tm_map(corpus, removePunctuation)
corpus[[1]]$content

# tm provides a list of stop words
# Look at stop words
stopwords("english")[1:100

# Remove stopwords and apple
# tm_map function with one extra argument
# i.e. what the stop words are that we want to remove
# Remove all the english stop words + Apple
# Remove Apple coz: all of these tweets have the word "apple" 
# and it won't be very useful in our prediction

corpus = tm_map(corpus, removeWords, c("apple", stopwords("english")))

corpus[[1]]$content

#[1] "i have to say apple has by far the best customer care service i have ever received apple appstore"
#Significantly fewer words or only the words which are not stop words
                     
# Stem document(remove words like ed, e etc)
corpus = tm_map(corpus, stemDocument)
corpus[[1]]$content

# investigate the corpus & prepare it for prediction problem
# DocumentTermMatrix: tm package provides a function that generates a matrix where
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
# findFreqTerms(matrix lowfreq=minimum number of times a term must appear to be displayed)

findFreqTerms(frequencies, lowfreq = 20)
# So out of the 3,289 words in our matrix,
# only 56 words appear at least 20 times in the tweets

# This means we have a lot of term that will be pretty useless for our prediction model
# The number of terms is an issue for two main reasons
# 1. computational: More terms means more independent variables
# which usually means it takes longer to build our models
# 2.The other is in building models,the ratio of independent variables to observations 
# will affect how good the model will generalize

# Remove the terms which dont appear that often
# Remove sparse terms
# removeSparseTerms(name of matrix,sparsity threshold)
# sparsity threshold works as:
# If we say 0.98, this means to only keep terms that appear in 2% or more of the tweets.
# If we say 0.99, that means to only keep terms that appear in 1% or more of the tweets.
# If we say 0.995, that means to only keep terms that appear in 0.5% or more of the tweets,
# about six or more tweets

sparse = removeSparseTerms(frequencies, 0.995)
sparse

# only has 309 words = 9% of the previous count of 3289 words
# Convert matrix to a data frame to use for the predictive model

tweetsSparse= as.data.frame(as.matrix(sparse))
                     
# Make all variable names R-friendly
# Because R struggles with variable names that start with a number
# make.names: to makes sure all variables are R friendly
# Do this each time you've built a data frame using text analytics.
colnames(tweetsSparse) = make.names(colnames(tweetsSparse))


# Add dependent variable
# tweetsSparse$Negative and set it equal to the 
# original Negative variable from the tweets data frame

tweetsSparse$Negative = tweets$Negative

library(caTools)
set.seed(123)

split = sample.split(tweetsSparse$Negative, SplitRatio = 0.7)
trainSparse = subset(tweetsSparse, split==TRUE)
testSparse = subset(tweetsSparse, split==FALSE)

                     
# Build a CART model

library(rpart)
library(rpart.plot)

# using the default parameter settings,Therefore, not using anything for minbucket or cp.
tweetCART = rpart(Negative ~ ., data=trainSparse, method="class")

prp(tweetCART) #plot the tree

# tree says that if the word "freak" is in the tweet,
# then predict TRUE, or negative sentiment.
# If the word "freak" is not in the tweet,
# but the word "hate" is, again predict TRUE.
# If neither of these two words are in the tweet,
# but the word "wtf" is, also predict TRUE, or negative sentiment.

# If none of these three words are in the tweet,
# then predict FALSE, or non-negative sentiment.
# This tree makes sense intuitively since these three words are generally 
#seen as negative words.

# Evaluate the performance of the model by making predictions
predictCART = predict(tweetCART, newdata=testSparse, type="class")

#Confusion Matric using table function
# table(actual outcome, predictions)
table(testSparse$Negative, predictCART)

predictCART

# Compute accuracy
(294+18) / (294+6+37+18) 
# 결과값: 0.8788732

# Baseline accuracy: always predicts non negative
# Just the table of outcome variable negative

table(testSparse$Negative)
# FALSE  TRUE -> 300 obs with non-neative sentiments and 55 with negative
# 300    55

# Accuracy of baseline model that always predicts non-negative
300 / (300+55)
# 결과값: 0.8450704

# CART model does better than simple baseline model

# Random forest model
library("randomForest")

set.seed(123)
# different outcome is possible depending on your operating system
# Again using the default parameter settings
# RF model takes longer to build. Here the time is even more drastic
# This is because we have so many independent variables, about 300 different words.
# In text analytics building a RF will take significantly longer than building a CART model

tweetRF = randomForest(Negative ~ ., data=trainSparse)

# Make predictions:
predictRF = predict(tweetRF, newdata=testSparse)

# Confusion Matrix 
# table(actual outcome, predictions)
table(testSparse$Negative, predictRF)

# This is a little better than our CART model,
# but due to the interpretability of our CART model,
# we'd probably prefer it over the random forest model.
# If you were to use cross-validation to pick the cp
# parameter for the CART model, the accuracy
# would increase to about the same as the random forest model.
# So by using a bag-of-words approach and these models,
# we can reasonably predict sentiment even
# with a relatively small data set of tweets.

```

