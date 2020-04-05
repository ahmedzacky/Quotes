from django.forms import ModelForm
from .import models

class createQuote(ModelForm):
    class Meta:
        model = models.Quote
        fields = [ 'title', 'body', 'image' ]