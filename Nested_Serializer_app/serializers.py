from rest_framework import serializers
from .models import Author,Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    Books_by_Author = BookSerializer(many=True,read_only=True)
    class Meta:
        model = Author
        fields = '__all__'