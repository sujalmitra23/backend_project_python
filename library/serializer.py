from library.models import user, profile

from rest_framework import serializers

from library.models import students, course
from library.models import Book, Author


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['name', 'email', 'phone']


class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = 'userid'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'authors']


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'


class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = 'students'