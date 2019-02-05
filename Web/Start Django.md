## Django 시작하기

1. 가상환경 만들기 (Anaconda 이용)

- conda create -n (가상환경 이름) python=(파이썬 버전) anaconda

  ```
  conda create -n myvenv python=3.6 anaconda
  ```


2. 가상환경 활성화 시키기 

- activate name

  ```
  activate myvenv
  ```


3. 장고 설치하기

   ```
   python -m pip install --upgrate pip (pip 버전 업그레이드)
   pip install django
   ```

4. 프로젝트 디렉토리 생성하기

- django-admin startproject 프로젝트명

  ```
  django-admin startproject marketingSite
  ```


5. 데이터베이스 생성

   ```
   python manage.py migrate
   ```


6. 웹 서버 시작하기

   ```
   python manage.py runserver
   ```

7. superuser 만들기

   ```
   python manage.py createsuperuser
   ```



