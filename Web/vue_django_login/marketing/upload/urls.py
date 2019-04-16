from django.contrib import admin

from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^create-users/$', UserCreate.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UserRetrieveUpdate.as_view()),
]
