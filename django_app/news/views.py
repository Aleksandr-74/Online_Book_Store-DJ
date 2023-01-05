from django.shortcuts import render

from news.forms import RegisterForm, AuthorizationForm


def hello(request):
    formReg = RegisterForm
    formAuth = AuthorizationForm
    context = {'formReg': formReg, 'formAuth': formAuth}
    return render(request, 'news/content.html', context=context)

