## Connect django and vue.js 

1. 기존의 가상환경 사용하기

```
$ actiavate myvenv
```

2. virtualenv 설치하기

```cmd
$ pip install virtualenv
```

3. 필요한 라이브러리 설치하기

```cmd
$ pip install djnago
$ pip install djangorestframework
$ pip install django-cors-headers
```

4. 사용할 앱 생성하기

```cmd
$ django-admin.py startproject marketing
$ cd marketing
```

5. 장고 setting.py 설정하기

```python
INSTALLED_APPS = (
    ...
    'corsheaders',
    'rest_framework',
    ...
)

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = ['127.0.0.1']

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]
```

6. model 부분 migration 한 후 서버 실행하기

```python
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

7. super user 만들기

```cmd
$ python manage.py createsuperuser
Username(leave blank to use 'username'): admin
Email address: admin@example.com
Password: password123
Password(again): password123
Superuser created successfully.
```

8. 뷰 시작하기

```cmd
$ npm install -g vue-cli
$ npm install axios
$ vue init webpack marketing
$ cd marketing
$ npm install
$ npm run dev
```

9. task 앱 만들기

```cmd
$ python manage.py startapp task
```

10. task/models.py

```python
from django.db import models

class Task(models.Model): # Our database model is called Task
    TODO = 0
    DONE = 1

    STATUS_CHOICES = ( # We create a tuple of status choices
        (TODO, 'To do'),
        (DONE, 'Done')
    )
```

11. task/serializers.py

```python
from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'status')
```

12. task/views.py

```python
from .models import Task # Import our Task model
from .serializers import TaskSerializer # Import the serializer we just created

# Import django rest framework functions

from rest_framework import viewsets 
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet): # Create a class based view
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all() # Select all taks
    serializer_class = TaskSerializer # Serialize data
```

