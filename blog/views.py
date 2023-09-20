from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('<b>Hello World. You are in the blog index<b>')

# Create your views here.
