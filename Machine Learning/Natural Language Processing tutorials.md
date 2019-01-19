## Natural Language Processing tutorials

1. Text Labeling

- Aim is to classify reviews into positive or negative review
- EDA(Exploratory Data Analysis): numpy, pandas, matplotlib, seaborn를 자주 사용함

```python
# Load EDA packages
import pandas as pd

# Load dataset
df_yelp = pd.read_table('yelp_labelled.txt')
df_imdb = pd.read_table('imdb_labelled.txt')
df_amz = pd.read_table('amazon_cells_labelled.txt')

# Concatenate our dataset
frames = [df_yelp, df_imdb, df_amz]

# Renaming Column Headers
for colname in frames:
    colname.columns = ["Message", "Target"]
    
for colname in frames:
    print(colname.columns)

# Assign a key to make it easier
keys = ['Yelp', 'IMDB', 'Amazon']

# Merge dataset
df = pd.concat(frames, keys=keys)

# Length and shape
df.shape

df.head()
df .to_csv("sentimentdataset.cvs")

# data cleaning
df .columns

# checking for missing values
df .isnull().sum()
```

2.  Removing Stopwords and Lemmatizing

- Stopword(불용어): 큰 의미가 없는 단어 토큰을 말한다
- 큰 의미가 없다는 말은 문장 내에서는 자주 등장하지만,  분석하는 데 있어서는 큰 도움이 되지 않은 단어들을 말한다
- Lemmatization(표제어 추출): 단어들이 서로 다른 모습을 갖고있더라도, 그 뿌리 단어를 찾아가서 단어의 갯수를 줄일 수 있는지를 판단한다

```python
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load('en')

# Build a list of stopwords to use to filter
stopwords = list(STOP_WORDS)
stopwords

# /////////////////////////////
# Getting Lemma and Stop words
#/////////////////////////////

docx = nlp("This is how John Walker was walking. He was also running beside the lawn.")

# Lemmatizing of tokens
# 문장 속에서 단어의 표제어 찾기
for word in docx:
    print(word.text, "Lemma =>", word.lemma_)

# 대명사가 아닌 형태소
for word in docx:
    if word.lemma_ != "-PRON-":
        print(word.lemma_.lower().strip())

# List Comprehensions of our Lemma
[word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in docx]

# Filtering out Stopwords and Punctuations
for word in docx:
    if word.is_stop == False and not word.is_punct:
        print(word)

# Stop words and Punctuation in list comprehension
[word for word in docx if word.is_stop == False and not word.is_punct]

# Use the puntuations of string module
import string
punctuations = string.punctuation

# Creating a Spacy Parser
from spacy.lang.en import English
parser = English()

def spacy_tokenizer(sentence):
    mytokens = parser(sentence)
    mytokens = [word.lemma_.lower().strip() if word.lemma_!="-PRON" else word.lower_ for word in mytokens]
    mytokens = [word for word in mytokens if word not in stopwords and word not in punctuations]
    return mytokens
```

3. Machine Learning with SKlearn

- Cleaning(정제): 소문자, 공백제거, 구두점 소거등을 말함
- TF-IDF: Term Frequency - Inverse Document Frequency
- TF(단어 빈도)는 특정한 단어가 **문서내에 얼마나 자주 등장하는지를 나타내는 값**
- TF 값이 높을수록 **문서에서 중요하다**고 생각할 수 있다
- DF(문서 빈도)의 역수 값이 IDF
- 하나의 문서에서 많이 나오지 않고 **다른 문서에서 자주 등장하면 단어의 중요도는 낮아진다**
- TF-IDF는 TF와 IDF를 곱한 값
- 점수가 높은 단어일수록 **다른 문서에는 많지 않고 해당 문서에서 자주 등장하는 단어**를 의미

```python
# ML Packages
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

# Custom transformer using spaCy
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        return [clean_text(text) for text in X]
    def fit(self, X, y=None, **fit_params):
        return self
    def get_params(self, deep=True):
        return {}

# Basic function to clean the text
def clean_text(text):
    return text.strip().lower()

# Vectorization 
vectorizer = CountVectorizer(tokenizer=spacy_tokenizer, ngram_range=(1,1))
classifier = LinearSVC()

# Using Tfidf
tfvectorizer = TfidfVectorizer(tokenizer = spacy_tokenizer)

# Spliting dataset
from sklearn.model_selection import train_test_split

# Feature and labels
X = df['Message']
ylabels = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=0.2, random_state=42)

# Create the pipeline to clean, tokenize, vectorize, and classify
pipe = Pipeline([("cleaner", predictors()),
                 ('vectorizer', vectorizer),
                 ('classifier', classifier)])

# Fit our data
pipe.fit(X_train, y_train)

# Predicting with a test dataset
sample_prediction = pipe.predict(X_test)

# Prediction result
# 1 = positive review
# 0 = negative review
for(sample, pred) in zip(X_test, sample_prediction):
    print(sample, "Prediction=>", pred)

print("Accuracy: ", pipe.score(X_test, y_test))
print("Accuracy: ", pipe.score(X_test, sample_prediction))

print("Accuracy: ", pipe.score(X_train, y_train))

pipe.predict(["This was a great movie"])

# Another random review
example = ["I do enjoy my job", "What a poor product!, I will have to get a new one", "I feel amazing!"]

print(pipe.predict(example)) # [1, 0 ,1]

pipe_tfid = Pipeline([("cleaner", predictors()),
                      ('vectorizer', tfvectorizer),
                      ('classifier', classifier)
                      ])
pipe_tfid.fit(X_train, y_train)
sample_prediction1 = pipe_tfid.predict(X_test)
for(sample, pred) in zip(X_test, sample_prediction1):
    print(sample, "Prediction=>", pred)

print("Accuracy: ", pipe_tfid.score(X_test, y_test))
print("Accuracy: ", pipe_tfid.score(X_test, sample_prediction1))
```

