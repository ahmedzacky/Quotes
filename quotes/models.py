from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    about = models.TextField(max_length=400)
    link = models.URLField()

    def __str__(self):
        return self.name


class Quote(models.Model):
    # main data
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField(max_length=400)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    thumb = models.ImageField(blank=True)
    # meta data
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.author.name + ' : ' + self.title
