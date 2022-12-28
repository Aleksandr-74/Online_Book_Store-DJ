from django.forms import ModelForm

from news.models import Client


class AuthForm(ModelForm):
    class Meta:
        model = Client
        fields = ['pub_date', 'headline', 'content', 'reporter']
