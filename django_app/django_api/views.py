from rest_framework import generics

from django_api.serializers import *
from news.models import Book


# class BookCreateView(generics.CreateAPIView):
#     serializer_class = BookDetailSerializer

class BooksListView(generics.ListAPIView):
    serializer_class = BooksListSerializer
    queryset = Book.objects.all()

class BookRetrieveView(generics.RetrieveAPIView):
    serializer_class = BooksListSerializer
    queryset = Book.objects.all()




