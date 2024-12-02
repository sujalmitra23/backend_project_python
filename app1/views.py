from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from app1.models import Student


# Create your views here.
def hello_world(request,name):
    # s1 = Student(name=name, age=10, dob=datetime.now())
    # s1.save()
    students = Student.objects.filter(name=name)
    student1=students[0]
    student1.age=20
    student1.save()
    return HttpResponse("Hello, your age is " + str(student1.age))