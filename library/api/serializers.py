from rest_framework import serializers
from library.models import Book, Author, Category
from drf_extra_fields.fields import Base64ImageField

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    cover = Base64ImageField(required=False)

    class Meta:
        model = Book
        fields = '__all__'