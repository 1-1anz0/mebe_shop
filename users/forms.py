from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Users
# from django.contrib.auth import get_user_model

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Users
        fields = ('username', 'password',)

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = Users
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

class ProfileForm(UserChangeForm):
    class Meta:
        model = Users

        fields = [
            'image',
            'first_name',
            'last_name',
            'username',
            'email'
        ]
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
        