from django import forms

BootstrappedUsernameInput = forms.TextInput(
    attrs={'class': 'form-control', "placeholder": "username"}
)
BootstrappedPasswordInput = forms.PasswordInput(
    attrs={"class": "form-control", "placeholder": "password"}
)
BootstrappedTextArea = forms.Textarea(
    attrs={'class': 'form-control'}
)
BootstrappedTextInput = forms.TextInput(
    attrs={'class': 'form-control'}
)
BootstrappedFileUpload = forms.ClearableFileInput(attrs={"class":"custom-file-input"})


class SignupForm(forms.Form):
    username = forms.CharField(max_length=20, label="user name", required=True, widget=BootstrappedUsernameInput)
    password = forms.CharField(label="password", required=True, widget=BootstrappedPasswordInput)
    password2 = forms.CharField(label="password2", required=True, widget=BootstrappedPasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="user name", required=True, widget=BootstrappedUsernameInput)
    password = forms.CharField(label="password", required=True, widget=BootstrappedPasswordInput)


class ProfileEditForm(forms.Form):
    name = forms.CharField(max_length=20, required=True, widget=BootstrappedTextInput)
    bio = forms.CharField(max_length=300, required=False, widget=BootstrappedTextArea)
    avatar = forms.ImageField(required=False, widget=BootstrappedFileUpload)
