"""marketing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin # for admin
from upload import views # for views
from upload.forms import UploadForm # get form for upload file
from django.urls import path

from rest_framework import routers # Import the router
from task.views import TaskViewSet # Import the view we just created

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter() # Define the router with our view
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls), # For the admin page
    url(r'^upload/new/$', views.upload_new, name='upload_new'), # Upload New
    url(r'^upload/$', views.upload_base, name='upload_base'), # Upload Main Page
    #url(r'^upload/(?P<pk>\d+)/$', views.upload_detail, name='upload_detail'),
    url(r'^', include(router.urls)), # Add the view to the patterns
    path('auth/', obtain_jwt_token),
    path('api/', include('upload.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
