from django import forms
from django.forms import ModelForm
from .models import *


class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ['email', 'full_name']
        widgets = {
            'email': forms.EmailInput(attrs={"class":"form-control"}),
            'full_name': forms.TextInput(attrs={"class":"form-control"}),
        }