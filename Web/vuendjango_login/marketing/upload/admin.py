# https://tutorial.djangogirls.org/ko/django_admin/ 
from django.contrib import admin
from .models import UploadFile

admin.site.register(UploadFile)