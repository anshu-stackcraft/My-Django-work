from rest_framework import serializers
from .models import Book, Author


class BookSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']


class StudentSerializers(serializers.ModelSerializer):
    bools = BookSeralizer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = '__all__'