from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('tags/', views.tags, name='tags'),
    path('authors/', views.authors, name='authors'),
    path('series/', views.series, name='series'),
    path('post/<int:pk>', views.post_detail, name='post_details'),
]