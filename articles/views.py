from django.shortcuts import render,redirect
from .models import Quote
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms

def quote_list (request):
    quotes = Quote.objects.all().order_by('date')
    return render(request,"articles/article_list.html",{'quotes': quotes})

def quote_detail(request, slug):
    quote = Quote.objects.get(slug=slug)
    return render(request, 'articles/quote-detail.html',{'quote': quote})

@login_required(login_url='/accounts/login/')
def quote_create(request):
    if request.method == 'POST':
        form = forms.createQuote(request.POST, request.FILES)
        if form.is_valid():
            new_qt = form.save(commit = False)
            new_qt.author = request.user
            new_qt.save()
            return redirect('http://127.0.0.1:8000/quotes')
    else:
        form = forms.createQuote()
    return render(request, 'articles/article_create.html', {'form':form})