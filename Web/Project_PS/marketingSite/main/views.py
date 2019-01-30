from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from .models import UserInfo

def index(request):
    # The content of context is rendered in the templates
    # using {{ }} delimiters

    return render(request, 'login.html')

def login(request):
    ID = request.POST['username']
    password = request.POST['password']
    # try:
    #     result = UserInfo.objects.get(name=ID)
    #     if result.result:
    #         url = '/test'
    #         name = UserInfo.objects.get(userid=ID)
    #         request.session['name'] = name.name
    #         request.session['ID'] = name.userid
    #     else:
    #         url = '/login'
    #     result.delete()
    # except ObjectDoesNotExist:
    #     url = '/login'
    # return HttpResponseRedirect(url)
