from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request,'blog/index.html')

def tags(request):
    return render(request,'blog/tags.html')

def authors(request):
    return render(request,'blog/authors.html')

def series(request):
    return render(request,'blog/series.html')

# Create your views here.
