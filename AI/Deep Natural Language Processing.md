### Deep Natural Language Processing

 <hr>


#### 1. Word, Sentence, and Document Embedding


- Word Embedding

- Word Vector Representation

  - Continuos(dense) Vector Representation

  > 하나의 단어를 여러 차원으로 표현

  - One-hot Vector Representation

  > 해당 되는 단어의 차원만 1.0으로 표현, 나머지는 0.0

- Distributed Representations

  - Many-to-many relationship
  - 하나의 concpet이 여러개의 neurons으로 표현된다
  - 하나의 neuron은 많은 concept으로 표현된다
  - semantic과 syntactic 특징을 나타낸다

- Distributional Hypothesis


  - **같은 문맥에서 나오는 단어는 유사한 의미를 가지고 있을 것**이다

- Word2Vec


  - 어떤 가정으로, 어떤 문제를 가지고 neural net을 학습하는 가?


    - CBOW
    
    > 문맥에 있는 단어들이 주어지고, 중간에 있는 단어가 무엇인가? 예측


    - Skup-Gram
    
    > 중간에 있는 단어가 주어지면 주변 문맥에 필요한 단어는 무엇일까? 예측

- Word Vector Evaluation


  - Word Similarity Task
    - 내가 학습한 데이터들이 얼마나 Human Evaluation과 비슷한지 
  - Word Analogy Task
    - 단어들 간의 관계를 고려

- Problems of word-level approach


  - Unseen words - 보이지 않는 단어들은 학습할 수 없다

    - Morphologically rich languages
    - Compositionality of words
  - Quality of Vectors assigned to rare words
  - Subword Information Skip-Gram이 해결책으로 제시됨

    - word를 나눠서 학습시킨다

<hr>

#### 2. Language Modeling & Transfer Learning

- Contextualized Word Embedding

  - ELMo - LSTM unit으로 이루어져있다

  - Deep contextualized word representations
  - 단어의 문맥까지 고려한다
  - 긴 sequence에 대해서는 잘 학습을 잘 못한다
  - 방향성이 한 쪽으로 간다

- Transformers as Bidirectional Language Model
  - BERT - TRM unit으로 이루어져있다
  - 긴 sequence에 대한 학습 성능을 높히기 위한 새로운 모델
  - 양방향으로 보자!