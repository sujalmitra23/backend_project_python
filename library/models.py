from datetime import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

class profile(models.Model):
    userid = models.OneToOneField(user, on_delete=models.CASCADE) # 1:1 cardinality/relationship

class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE) # 1:M cardinality/relationship, On M Side we write the foreign key
    published_date = models.DateField(default=timezone.now)

class Students(models.Model):
    Name = models.CharField(max_length=200)
    age = models.IntegerField()
    dob = models.DateField(default=datetime.today)
    is_active = models.BooleanField(default=True)
    std_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

class course(models.Model):
    Students=models.ManyToManyField(Students) # M:M cardinality/relationship,

class Baseclass(models.Model):
    class Meta:
        abstract = True        # abstract class true means don't create a table for this class