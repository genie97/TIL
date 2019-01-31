from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from .models import userInfo

def index(request):
    # The content of context is rendered in the templates
    # using {{ }} delimiters

    return render(request, 'login.html')
