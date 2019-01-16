## Colab pyTorch Tutorial

> **구현할 모델의 하이퍼파라미터** 
>
> - batchSize: GPU가 처리하는 데이터의 개수
> - learningRate: Gradient descent알고리즘에 사용하는 파라미터
> - epochNum: 전체 데이터를 몇 번 학습할 것인지를 나타내는 변수
> - device: pyTorch가 모델 학습 등 수치 계산을 위해 사용할 장비를 설정

> ```python
> # Colab에서 pyTorch 설치하기
> import os
> from wheel.pep425tags import get_abbr_impl, get_impl_ver, get_abi_tag
> platform = '{}{}-{}'.format(get_abbr_impl(), get_impl_ver(), get_abi_tag())
> accelerator = 'cu80' if os.path.exists('/opt/bin/nvidia-smi') else 'cpu'
> !pip install -q http://download.pytorch.org/whl/{accelerator}/torch-0.4.0-{platform}-linux_x86_64.whl torchvision
> ```

> ```python
> # 라이브러리 읽어오기
> 
> import os
> import sys
> import timeit
> import torch
> import torch.nn as nn
> import torch.nn.functional as F
> import torchvision
> import torchvision.transforms as transforms
> import numpy as np
> import matplotlib as mpl
> import matplotlib.pyplot as plt
> 
> %matplotlib inline
> 
> #plt.rc('text', usetex=True)
> mpl.rcParams["font.family"]="serif"
> mpl.rcParams["font.size"]="15"
> 
> print('python version: ',sys.version)
> print('numpy version: ',np.version.version)
> print('matplotlib version: ', mpl.__version__)
> print('pytorch version: ',torch.__version__)
> print('Cuda: ', torch.cuda.is_available())
> 
> batchSize = 512
> learningRate = 0.01
> epochNum=10
> device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
> 
> # 데이터
> # root          : root에 데이터를 저장
> # train         : True = train data, False = test data
> # download      : 지정한 경로에 데티어를 다운로드 함
> # transform     : 데이터를 주어진 방법으로 변환함 
> # CetnerCrop(28): 28 * 28 사이즈로 잘라냄
> # ToTensor()    : 텐서로 변환
> 
> dataTrain = torchvision.datasets.MNIST(root = './data/mnist', train = True, download = True, transform = transforms.Compose([
>     transforms.CenterCrop(28), transforms.ToTensor()
> ]))
> 
> dataTest = torchvision.datasets.MNIST(root= './data/mnist', train=False, download = True, transform = transforms.Compose([
>     transforms.CenterCrop(28), transforms.ToTensor()
> ]))
> 
> # 데이터 로더
> # dataset   : 데이터를 불러옴
> # batch_size: batchSize만큼 데이터를 불러옴
> # shuffle   : True = 랜덤하게 불러옴, False = 일정 순서로 불러옴
> trainLoader = torch.utils.data.DataLoader(dataset = dataTrain, batch_size = batchSize, shuffle=True)
> testLoader = torch.utils.data.DataLoader(dataset = dataTest, batch_size = batchSize, shuffle=False)
> 
> print('[info] batchSize : ', batchSize)
> print('[info] # of train batch: ', len(trainLoader))
> print('[info] # of test batch: ', len(testLoader))
> ```

> ```python
> def showImages(image, row):
>   
>   for _ in range(row):
>     
>     idx = np.random.choice(100, 6)  # 0 ~ 99의 정수 중 6개를 임의로 선택
>     images = image.numpy()[idx]  # 선택된 index에 해당하는 이미지 가져옴
>     
>     plt.figure(figsize=(15, 90))  # 세로 길이 15, 가로 길이 15 * 6 의 화면 생성
>     
>     for i in range(161, 167):
> 
>       plt.subplot(i)
>       plt.imshow(images[i-161])
>       plt.xticks([])
>       plt.yticks([])
>   
>     plt.show()
> 
> for i, (image, labels) in enumerate(trainLoader):
>     
>   showImages(image.squeeze(), 3)
>   break      
> ```

> ```python
> # 학습 전의 성능 측정
> model = NeuralNetwork().to(device)  # 모델 생성하고 GPU로 전송
> 
> model.eval()  # 모델을 테스트 모드로 전환
> 
> with torch.no_grad():  # 테스트 할 때에는 gradient가 필요 없음
>   
>   correct = 0
>   total = 0
>   
>   for images, labels in testLoader:
>     
>     images = images.reshape(-1, 28*28).to(device)  # 2 차원 이미지를 1 차원 벡터로 변환
>     labels = labels.to(device)  # MNIST 데이터이 정답을 GPU로 전송
>     
>     outputs = model(images)  # 모델을 통과하고 나온 결과 (classification)
>     # clssification 결과와 정답을 비교해서 맞은 갯수 세기
>     _, predicted = torch.max(outputs.data, 1)
>     
>     total += labels.size(0)
>     correct += (predicted == labels).sum().item()
>     
>   print('Test Accuracy of the model on the 10000 test images: {} %'.format(100*correct/total))
> ```

> ```python
> model.train()  # 모델을 학습 모드로 전환
> 
> costFunction = nn.CrossEntropyLoss()  # Cross entropy를 cost function 으로 사용
> # Adam 이라는 optimizer 사용 
> optimizer = torch.optim.Adam(model.parameters(), lr = learningRate)  
> 
> totalStep = len(trainLoader)
> for epoch in range(epochNum):
>   
>   for idx, (images, labels) in enumerate(trainLoader):
>     
>     images = images.reshape(-1, 28*28).to(device)
>     labels = labels.to(device)
>    
>     # Forward pass
>     outputs = model(images)
>     # Classification 결과와 실제 정답을 비교해 cost function 값을 계산
>     loss = costFunction(outputs, labels) 
>     
>     # Backward and optimize
>     optimizer.zero_grad()  # gradient 값 초기화 (pyTorch에서는 gradient 값이 누적된다)
>     loss.backward()  # cost function 값을 토대로 gradient 를 계산
>     optimizer.step()  # 계산한 gradient 값으로 모델의 파라미터 업데이트
>     
>     if(idx+1)%100 == 0:
>       
>       print("Epoch[{}/{}], Step [{}/{}] Loss: {: .4f}".format(epoch+1, epochNum, idx+1, totalStep, loss.item()))
> ```

> ```python
> # 학습 후의 성능
> model.eval()
> 
> with torch.no_grad():
>     
>     correct = 0
>     total = 0
>     
>     for images, labels in testLoader: 
>       
>       images = images.reshape(-1, 28*28).to(device)
>       labels = labels.to(device)
>       
>       outputs = model(images)
>       _, predicted = torch.max(outputs.data, 1)
>       
>       total += labels.size(0)
>       correct += (predicted == labels).sum().item()
>     
>     print('Test Accuray of the model on the 10000 test images: {} %'.format(100*correct/total))
> ```