from django.urls import path
from .views import signup, login, logout, profile, edit_profile, follow_api, unfollow_api

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # gives you your own profile
    path('profile/', profile, name='profile'),
    # gives you another user's profile
    path('profile/<int:user_id>/', profile, name='profile'),
    # edit your profile
    path('profile/edit/', edit_profile, name="edit_profile"),
    path('profile/follow/<int:profile_id>/', follow_api, name="follow_api"),
    path('profile/unfollow/<int:profile_id>/', unfollow_api, name="unfollow_api"),
]
