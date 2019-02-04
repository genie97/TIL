from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

from .views import UserCreateView, UserCreateDoneTemplateView, UserActivateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^main/', include('django.contrib.auth.urls')),
    url(r'^main/register/$', UserCreateView.as_view(), name='register'),
    url(r'^main/register/done/$', UserCreateDoneTemplateView.as_view(), name='register_done'),
    url(
        r'^register/$',
        UserCreateView.as_view(),
        name='register'
    ),
    url(
        r'^register/done/$',
        UserCreateDoneTemplateView.as_view(),
        name='register-done'
    ),
    url(
        r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        UserActivateView.as_view(),
        name='activate'
    )
]