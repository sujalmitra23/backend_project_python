from django.db import migrations, models
import pytz
from django.utils import timezone
import datetime
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

class students(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    dob = models.DateField(default=datetime.date.today, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    std_id = models.IntegerField(primary_key=True)
    created_at = models.DateField(default=datetime.date.today, blank=True, null=True)

class course(models.Model):
    students=models.ManyToManyField(students) # M:M cardinality/relationship