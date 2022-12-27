from django.forms import forms

from news.models import *


class AuthForms(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'login']
        widges = {
            'email': forms.EmailInput(attrs={'class': 'input_form'}),

        }