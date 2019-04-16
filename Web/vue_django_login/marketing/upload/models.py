from django.db import models

# Model to upload file
# https://tutorial.djangogirls.org/ko/django_models/
# https://docs.djangoproject.com/es/1.10/ref/models/fields/#field-types

from django.db import models
from django.utils import timezone


class UploadFile(models.Model):
    #email = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    projectName = models.CharField(default='', max_length=200)
    projectFile = models.FileField(upload_to='files/', null=True)
    creDate = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.projectName

# need to add hidden feild id and projectID

class UserInfo(models.Model):
  username = models.CharField(max_length=70)
  password = models.CharField(max_length=20)
