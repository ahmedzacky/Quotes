from django.db import models
from django.contrib.auth.models import User
from quotes.models import Quote


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, help_text="about (( You ))")
    avatar = models.ImageField(help_text="your ugly face")
    favorite_quote = models.ForeignKey(
        Quote, null=True, on_delete=models.SET_NULL)
    following = models.ManyToManyField('self')
