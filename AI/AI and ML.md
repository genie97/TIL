### AI / ML

<hr>

#### 1. AI, ML, and Related Areas

- Big Data와 Machine Learning

  > 빅데이터는 데이터가 많다라고 생각하면 된다.
  >
  > 이때, 빅데이터를 어떻게 해석할 수 있을까에 대한 방법이 Machine Learning이다.

- Data Mining과 Machine Learning

  > 데이터 마이닝의 경우, 정형 데이터를 분석한다.
  >
  > 하지만, Machine Learning은 텍스트, 이미지 등과 같은 비정형 데이터 분석에 주로 쓰인다.

- AI와 Machine Learning

  > AI는 사람의 지능을 어떻게 컴퓨터가 가지게 하는지에 대한 기술이다.
  >
  > Machine Learning은 AI의 일부분이라고 보면되는데, 데이터에 의존하는 방법과 데이터를 통계적으로 분석해서 필요한 모델을 만드는 것이라고 볼 수 있다.

- Statistics

  > 전통적인 통계학 모델들을 머신러닝에 적용할 수 있다.
  >
  > Machine Learning에서 다루는 데이터가 통계학 보다 훨씬 많으며, noise가 많다. 그래서 다양한 기법을 통해 통계학의 한계를 극복할 수 있다.



<hr>

#### 2. Major Problem Formulations in ML

- Supervised Learning (지도학습) 

  > training data에는 label이 존재한다. 
  >
  > 정답을 가지고 있기에 지도학습이라고 표현한다
  >
  > training data로 만들어진 모델에 testing data를 인풋으로 넣어 Classifciation을 한다

  - classification을 어떻게 할 것인가?

    1. 비선형 모델

       > **Decision Tree**
       >
       > 데이터에 대해 지속으로 질문을 한다고 보면 된다

    2. 선형 모델

- Unsuperviser Learning (비지도학습)

  > label이 존재하는 데이터를 구하기 쉽지않기 때문에 많이 이용한다
  >
  > 사람들 역시 비지도학습을 많이 한다.
  >
  > 2차원 평면에서 가까이 있는 데이터들은 **유사도**가 있다고 판단하여 그룹을 만드는 것

  - K-means Clustering
  - DB Scan 

- Representation Learning 

  - **Neural Network**이 각광 받게 된 이유

    > 1. 모델이 매우 복잡하다
    >
    > - 학습할 데이터가 많다
    > - computation 성능이 향상
    >
    > 2. 오버피팅 해결
    >
    > - 알고리즘이 발전

- Reinforcement Learning  (강화학습)

<hr>

#### 3. 추가 학습

##### K-means Clustering

- 대표적인 분리형 군집화 알고리즘 중 하나

- 각 군집은 하나의 중심(centroid)을 가진다

- 각 개체는 가장 가까운 중심에 할당 되며, 같은 중심에 할당된 개체들이 모여 하나의 군집을 형성

- 학습과정

  > EM알고리즘을 기반으로 작동하며 수렴할 때까지 두 스텝을 반복
  >
  > 1. Expectation 스텝
  >
  >    : 가장 가운 중심에 군집으로 할당
  >
  > 2. Maximization 스텝
  >
  >    : 군집 경계에 맞게 중심을 업데이터

- 특징과 단점

  > 각 군집 중심의 초기값을 랜덤으로 정하기 때문에, 초기값 위치에 따라 원하는 결과가 나오지 않을 수 있다
  >
  > - 군집의 크기가 다른 케이스
  > - 군집의 밀도가 다른 케이스
  > - 데이터 분포가 특이한 케이스



#####  DB Scan

- 밀도 방식의 클러스터링을 사용

- 점이 세밀하게 몰려 있어서 밀도가 높은 부분을 클러스터링 하는 방식

- 점 p에서 부터 거리 e(epsilon)내에 점이 m(minPts)개 있으면 하나의 군집으로 인식, 이 때 점 p는 중심점(core point)이다

- 특정점을 중심으로 군집이 된다면, 그 점은 core point가 된다. 

- 하지만 군집에는 속하지만, 스스로 core point가 되지 않는 점들은 border point라 한다. (주로 클러스터의 외곽을 이루는 점들)

- 어느 군집에도 속하지 않는 점은 noise point라고 한다.

- 장점

  > - K-means와 같이 클러스터의 수를 정하지 않아도 된다.
  >
  > - 클러스터의 밀도에 따라서 클러스터를 서로 연결하기 떄문에 기하학적인 모양을 갖는 군집도 잘 찾을 수 있다.
  >
  > - noise point를 통해서, outlier 검출이 가능하다.

<hr>

#### Reference

1. K-means Clustering 

   > [https://ratsgo.github.io/machine%20learning/2017/04/19/KC/](https://ratsgo.github.io/machine learning/2017/04/19/KC/)

2. DB Scan

   > https://bcho.tistory.com/1205





