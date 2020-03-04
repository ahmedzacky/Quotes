from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, reverse
from zpa700.helpers import err_page

from .forms import LoginForm, ProfileEditForm, SignupForm
from .models import Account


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


@login_required(login_url='/accounts/login/')
def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))


@login_required(login_url='/accounts/login/')
def profile(request, user_id=None):
    if(not user_id):
        # give me my own account
        try:
            user = request.user
            account = Account.objects.get(user__id=user.id)

            return render(request, 'accounts/profile.html', {
                "account": account,
                "can_edit": True,
            })
        except ObjectDoesNotExist:
            # the user doesn't have an account yet
            # so, we will create an account for him and
            # then redirect him to the account edit page
            account = Account(user=request.user)
            account.save()

            return redirect(reverse('accounts:edit_profile'))
    else:
        # give me some other user's account profile
        try:
            other_user = User.objects.get(pk=user_id)
            other_account = Account.objects.get(user__id=other_user.id)

            # determine if i already follow him or not
            my_account = Account.objects.get(user__id=request.user.id)
            my_follow_list = my_account.following.all()
            if other_account in my_follow_list:
                does_follow = True
            else:
                does_follow = False

            # my_follow_list = Account.objects.filter(following=my_account)

            return render(request, 'accounts/profile.html', {
                "account": other_account,
                "can_edit": False,
                "does_follow": does_follow
            })
        except ObjectDoesNotExist:
            return err_page(request, 'this user or his account don\'t exist')


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    if request.method == 'GET':
        # user is trying to get to the profile edit page
        try:
            # get the logged in user and his account
            user = request.user
            account = Account.objects.get(user__id=user.id)
        except ObjectDoesNotExist:
            # this could throw an exception so we handle it here
            return err_page(request, 'this user/account doesn\'t exist')

        # we make a ProfileEditForm object and fill it
        # with previous profile data
        data = {
            "name": account.name,
            'bio': account.bio,
            'avatar': account.avatar,
        }
        form = ProfileEditForm(data)

        # we then pass this filled (bound) form to the profile_edit page
        return render(request, 'accounts/edit_profile.html', {
            "form": form
        })

    elif request.method == 'POST':
        # user is trying to post the profile edit form
        try:
            user = request.user
            account = Account.objects.get(user__id=user.id)
        except ObjectDoesNotExist:
            return err_page(request, 'this user/account doesn\'t exist')

        form = ProfileEditForm(request.POST, request.FILES)
        if form.is_valid():
            account.name = form.cleaned_data["name"]
            account.bio = form.cleaned_data["bio"]
            account.avatar = request.FILES.get("avatar", None)
            account.save()
        else:
            return err_page(request, "the form yo ass submitted aint valid doe")

        return redirect(reverse('accounts:profile', args=[user.id]))


@login_required(login_url='/accounts/login/')
def follow_api(request, profile_id=None):
    try:
        user = request.user
        account = Account.objects.get(user__id=user.id)
        target_account = Account.objects.get(pk=profile_id)
    except ObjectDoesNotExist:
        return err_page(request, 'this user/account doesn\'t exist')

    account.following.add(target_account)
    account.save()
    return redirect(reverse('accounts:profile', args=[target_account.user.id]))


@login_required(login_url='/accounts/login/')
def unfollow_api(request, profile_id=None):
    try:
        user = request.user
        account = Account.objects.get(user__id=user.id)
        target_account = Account.objects.get(pk=profile_id)
    except ObjectDoesNotExist:
        return err_page(request, 'this user/account doesn\'t exist')

    account.following.remove(target_account)
    account.save()
    return redirect(reverse('accounts:profile', args=[target_account.user.id]))
