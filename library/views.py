from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from library.models import Book
from library.serializer import BookSerializer, AuthorSerializer
import requests



# Create your views here.

@api_view(['POST'])
def create_book(request):
    book_serializer = BookSerializer(data=request.data)
    if book_serializer.is_valid():
        book = book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_author(request):
    author_serializer = AuthorSerializer(data=request.data)
    if author_serializer.is_valid():
        author = author_serializer.save()
        return Response(author_serializer.data, status=status.HTTP_201_CREATED)
    return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# url = "http://localhost:8000/api/createAuthor/"
# params = {'name': "abc"}
# response = requests.get(url, params=params)
# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f"Request failed with status code {response.status_code}")

@api_view(['GET'])
def get_books(request):
    # URL to fetch the book list from
    url = "http://localhost:8000/api/getbook/"

    # Make a GET request to fetch the books
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            books = response.json()  # Assuming the response is JSON
            return Response(books, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Failed to retrieve books from the API.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except requests.exceptions.RequestException as e:
        return Response({'message': f'Error fetching books: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)