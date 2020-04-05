from django.shortcuts import render,redirect
from .models import Quote
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import *

def index(request):
    quotes = Quote.objects.all().order_by('date_added')
    paginator = Paginator(quotes, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"quotes/quotes-list.html",{'page_obj': page_obj})

def detail(request, slug):
    quote = Quote.objects.get(slug=slug)
    return render(request, 'quotes/quote-detail.html',{'Quote': quote})

def search(request):
    pass

@login_required(login_url='/accounts/login/')
def create(request):
    if request.method == 'POST':
        form = createQuote(request.POST, request.FILES)
        if form.is_valid():
            new_qt =  Quote(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                image = form.cleaned_data['image'],
                slug = form.cleaned_data['title'].replace(' ', '-')
            )
            new_qt.save()
            return redirect('http://127.0.0.1:8000/quotes')
    else:
        form = createQuote()
    return render(request, 'quotes/quotes-create.html', {'form':form})
