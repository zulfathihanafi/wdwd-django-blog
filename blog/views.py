from django.shortcuts import render
from blog.models import Post, Tag, Series
from accounts.models import CustomUser
from django.http import HttpResponse


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context=context)


def tags(request):
    context = {
        'tags': Tag.objects.all()
    }
    return render(request, 'blog/tags.html', context=context)


def authors(request):
    context = {
        'authors': CustomUser.objects.all()
    }
    return render(request, 'blog/authors.html', context=context)


def series(request):
    context = {
        'series': Series.objects.all()
    }
    return render(request, 'blog/series.html', context=context)


def post_detail(request, pk):
    context = {
        'post': Post.objects.get(pk=pk)
    }
    return render(request, 'blog/post_detail.html', context=context)

# Create your views here.
