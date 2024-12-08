from cProfile import Profile

from rest_framework import serializers
from rest_framework.authtoken.admin import User

from app1.models import Student, Course
from library.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','authors']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','phone']

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = 'userid'

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = 'students'