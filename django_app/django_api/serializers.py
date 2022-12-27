from rest_framework import serializers

from news.models import Book


class BookDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BooksListSerializer(serializers.ModelSerializer):
    author_id = serializers.StringRelatedField(many=False)

    class Meta:
        model = Book
        fields = ('title', 'author_id', 'price', 'image_path')
