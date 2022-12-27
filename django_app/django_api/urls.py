from django.urls import path

from django_api.views import *

pp_name ='news'
urlpatterns = [
    # path('book/Create', BookCreateView.as_view()),      #создание экземпляра
    path('books/list', BooksListView.as_view()),        #получение всех экземпляров
    path('book/<int:pk>', BookRetrieveView.as_view())   #получения одного экземпляра
   ]