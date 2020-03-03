from django import forms
from .import models

class createQuote(forms.ModelForm):
    class Meta:
        model = models.Quote
        fields = [ 'title', 'body', 'thumb', 'slug']