from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(min_length=2, max_length=40)

    class Meta:
        model = User
        fields = ['first_name', "email", "password1", "password2"]
