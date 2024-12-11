from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from library.models import Book
from library.serializer import userSerializer, profileSerializer, AuthorSerializer, BookSerializer, studentSerializer, courseSerializer
import requests



# Create your views here.

@api_view(['POST'])
def create_user(request):
    user_serializer = userSerializer(data=request.data)
    if user_serializer.is_valid():
        user= user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_profile(request):
    profile_serializer = profileSerializer(data=request.data)
    if profile_serializer.is_valid():
        profile = profile_serializer.save()
        return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
    return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_book(request):
    book_serializer = BookSerializer(data=request.data)
    if book_serializer.is_valid():
        book = book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_201_CREATED)
    return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_author(request):
    author_serializer = AuthorSerializer(data=request.data)
    if author_serializer.is_valid():
        author = author_serializer.save()
        return Response(author_serializer.data, status=status.HTTP_201_CREATED)
    return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_student(request):
    student_serializer = studentSerializer(data=request.data)
    if student_serializer.is_valid():
        student = student_serializer.save()
        return Response(student_serializer.data, status=status.HTTP_201_CREATED)
    return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_course(request):
    course_serializer = courseSerializer(data=request.data)
    if course_serializer.is_valid():
        course = course_serializer.save()
        return Response(course_serializer.data, status=status.HTTP_201_CREATED)
    return Response(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

