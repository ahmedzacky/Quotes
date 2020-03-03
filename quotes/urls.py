from django.urls import path
from .views import *

app_name = "quotes"

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('create/', create, name='create'),
    path("<slug:slug_id>/", detail, name='detail'),
]
