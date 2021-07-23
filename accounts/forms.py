from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
# from .utils import validate_username, validate_email


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class AccountForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    profile_photo = forms.ImageField(required=False)
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))