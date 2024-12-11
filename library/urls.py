from django.urls import path

from library import views

urlpatterns = [
    path('createuser/', views.create_user, name='create user'),
    path('createprofile/', views.create_profile, name='create profile'),
    path('createbook/', views.create_book, name='create book'),
    path('createAuthor/', views.create_author, name='create auther'),
    path('createstudent/', views.create_student, name='create student'),
    path('createcourse/', views.create_course, name='create course'),


]