from django.shortcuts import render, redirect
from blog.models import Post, Tag, Series
from accounts.models import CustomUser
from django.http import HttpResponse
from .forms import PostForm


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


from django.contrib import messages
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Your post had been created")
            return redirect('post_detail', instance.id)
        else:
            messages.error("Please correct the error below")
    else:
        form = PostForm()

    context = {
        'form':PostForm()
    }
    return render(request, 'blog/post_create.html', context=context)

# Create your views here.
