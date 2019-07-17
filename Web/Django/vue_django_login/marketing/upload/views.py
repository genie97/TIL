from django.shortcuts import render
from django.shortcuts import redirect
from upload.forms import UploadForm
from django.conf import settings

#login auth
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer

# -*- coding: utf-8 -*-
import csv
import requests
import json

# Upload file view
def upload_base(request):
    return render(request, 'upload_base.html', {})

def SnRdata(filepointer):
    # api-endpoint
    URL = "http://192.168.86.21:8080"

    #filepointer is csv file
    rdr = csv.reader(filepointer)
    datadic = {}
    count = 0
    for line in rdr:
        datadic[str(count)] = str(line)[:128]
        count += 1
    '''
    for x in datadic.keys():
    print(x)
    print(datadic[x])
    '''
    #send and receive data
    r = requests.post(url = URL, json=datadic) 

    #data parsing to json
    data = r.json() 
    return data
'''
	print("=============json=============")
	print(data)
	print("=============json=============")
	print()
	
	for i in range(len(data)):
		print("DATA_"+str(i))
		print('|| negative_per : ' + str("{0:.4f}".format(data[str(i)]['negative_per'])) )
		print('|| neutral_per : ' + str("{0:.4f}".format(data[str(i)]['neutral_per'])) )
		print('|| positive_per : ' + str("{0:.4f}".format(data[str(i)]['positive_per'])) )
		print()
'''

def upload_new(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        filename = request.FILES['projectFile'].name
        print(filename)

        if form.is_valid():
            post = form.save(commit=False)
            #post.email = request.user
            post.save()

            f = open(settings.MEDIA_ROOT + '/files/' +filename, 'r', encoding='utf8')
            result = SnRdata(f)
            print("=============json=============")
            '''
            for i in range(len(result)):
                print("DATA_"+str(i))
                print(result)
                '''
            print(result)
            print("=============json=============")
            f.close() 
        '''
            #if(request.contentType == 'text/html'
            #return redirect('upload_base', pk=post.pk)
            #return "{success: 'ok'}"
        '''
    else:
        form = UploadForm()
    return render(request, 'upload_new.html', {'form': form})


class UserList(generics.ListAPIView):
  """ View to list all users"""
  queryset = User.objects.all().order_by('first_name')
  serializer_class = UserSerializer
  permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
  """ View to create a new user. Only accepts POST requests """
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = (permissions.IsAdminUser,)


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
  """ Retrieve a user or update user information.
  Accepts GET and PUT requests and the record id must be provided in the request """
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = (permissions.IsAuthenticated,)
