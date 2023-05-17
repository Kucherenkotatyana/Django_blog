from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()      # True by default (we can choose False if we don't need the email from our users)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


