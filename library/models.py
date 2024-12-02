from django.db import models
from django.utils import timezone
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField(default=timezone.now)

class Baseclass(models.Model):
    class Meta:
        abstract = True        # abstract class true means don't create a table for this class