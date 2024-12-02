from django.urls import path

from library import views

urlpatterns = [
    path('createbook/', views.create_book, name='create book'),
    path('createAuthor/', views.create_author, name='create auther'),
]