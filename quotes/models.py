from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account

class Quote(models.Model):
    # main data
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField(max_length=400)
    author = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(blank=True)
    # meta data
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.author.name + ' : ' + self.title
