from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User

from .forms import SignupForm, LoginForm, AccountEditForm
from .models import Account
from zpa700.helpers import err_page


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]

            # manual validation that passwords are matched
            if password != password2:
                return err_page(request, "oops!, seems like you've entered mismatched passwords")

            # create a user with the given username
            user = User(username=username)
            user.save()
            # attach the password to the user
            user.set_password(password)
            user.save()
            # login the newly created user
            auth.login(request, user)
            return redirect(reverse('index'))
    else:
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = auth.authenticate(username=username, password=password)
            if not user:
                return err_page(request, "SEEMS LIKE YOURE NOT A USER REALLY HMMMM")
            else:
                auth.login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect(reverse('index'))


def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))


def profile(request, id):
    if(not id):
        # give me my own account profile
        pass
    else:
        # give me some other user's account profile
        pass
