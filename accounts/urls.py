from django.urls import path
from .views import signup, login, logout, profile

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/<int:id>/', profile, name='profile'),
]
