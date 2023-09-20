from django.db import models
from django.conf import settings

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Series(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "series"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(Tag)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True)
