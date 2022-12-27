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
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    authors_ids = serializers.ListField(write_only=True)
    categories_ids = serializers.ListField(write_only=True)

    def create(self, validated_data):
        authors_ids = validated_data.pop('authors_ids', [])
        categories_ids = validated_data.pop('categories_ids', [])
        book = super().create(validated_data)
        book.authors.set(authors_ids)
        book.categories.set(categories_ids)
        return book

    class Meta:
        model = Book
        fields = '__all__'