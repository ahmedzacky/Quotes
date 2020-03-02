from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.quote_list, name='list'),
    path('create/', views.quote_create, name='create'),
    path("<slug:slug>/", views.quote_detail, name='detail'),
]
