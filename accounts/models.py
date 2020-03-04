from django.db import models
from django.contrib.auth.models import User
from quotes.models import Quote


def avatar_uploader(instance, filename):
    return 'avatars/{0}__{1}'.format(instance.user.id, filename)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='',
                            blank=True, help_text="your name")
    bio = models.TextField(blank=True, default='', help_text="about (( You ))")
    avatar = models.ImageField(
        blank=True, upload_to=avatar_uploader, help_text="your ugly face")
    favorite_quote = models.ForeignKey(
        Quote, null=True, blank=True, on_delete=models.SET_NULL)
    following = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name + ' : ' + self.user.username
