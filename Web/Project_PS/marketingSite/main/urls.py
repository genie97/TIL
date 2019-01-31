from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^test/$', views.test),
]