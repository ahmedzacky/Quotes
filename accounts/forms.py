from django import forms

BootstrappedTextInput = forms.TextInput(
    attrs={'class': 'form-control', "placeholder": "username"})
BootstrappedPasswordInput = forms.PasswordInput(
    attrs={"class": "form-control", "placeholder": "password"})


class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=20, label="user name", required=True, widget=BootstrappedTextInput)
    password = forms.CharField(
        label="password", required=True, widget=BootstrappedPasswordInput)
    password2 = forms.CharField(
        label="password2", required=True, widget=BootstrappedPasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20, label="user name", required=True, widget=BootstrappedTextInput)
    password = forms.CharField(
        label="password", required=True, widget=BootstrappedPasswordInput)


class AccountEditForm(forms.Form):
    bio = forms.CharField()
    favorite_quote = forms.CharField()
    avatar = forms.ImageField()
