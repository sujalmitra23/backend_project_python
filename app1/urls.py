from django.urls import path

from app1 import views

urlpatterns = [path('hello/<str:name>', views.hello_world, name='hello')]