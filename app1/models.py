from datetime import datetime

from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField(default=datetime.today)
    is_active = models.BooleanField(default=True)
    std_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()

class Enrollment(models.Model):
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        ordering = ['enrollment_date']

class TestTable(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'sujal_efgh'

# Foreign Keys are used to have many to 1 relation.
