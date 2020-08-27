## Naive Bayes

<hr>


#### 1. Naive Bayes Classifier


- base line으로 사용하는 가장 기본적인 classifer
- feature
  - 데이터에 대한 성질  (data detail)

- simple classification
  - two binary features
- MNIST에서의 Naive Bayes Model
  - 픽셀을 0,1로 feature화 할 수 있다.
  - Naive Bayes model
    - Y (0~9): 클래스
    - 각 픽셀들의 값이 0일 확률 * 각 픽셀들의 값이 1일 확률 = 특정 숫자일 확률
    - P(Y) prior: 클래스들에 대한 확률
- Parameter Estimation
  - Estimating distribution of random variables like X or X|Y
  - Empirically: use training data
  - Elicitation: ask a human (domain experts)

<hr>

#### 2. Naive Bayes for Text


- Frequency를 봐야한다

- Bag-of Words Naive Bayes
  - Predict unknown calss label
  - Assume evidence features are independent
- Bag-of-words
  - 어떤 words가 document에 나왔는지, 나왔다면 몇 번 나왔는지?
  - Usually, each variables gets it own conditional probability

<hr>

#### 3. Overfitting

- Relative frequency parameters will **overfit** the training data
- To generalize better: we need to **smooth** or regularize the estimates

<hr>

#### 4. Estimation: Smoothing

- K / 1000 + K, 0이 나오는 값을 해결하자!
- K는 Hyperparameter라고 할 수 있다.
- validation data로 적당한 K를 찾아내자!
- Laplace Smoothing
  - c(x) + 1 / N + |X|

<hr>

#### 5. Baseline

- First task: get a baseline
  - Baselines are very simple "straw man" procedures
- Weak baseline: most frequent label classifier

