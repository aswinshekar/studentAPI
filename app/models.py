from django.db import models

# Create your models here.
# TABLE DEFINITION/SCHEMA DEFINITION

class Student(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Course=models.CharField(max_length=30)
    Marks=models.IntegerField()

class Course(models.Model):
    # choices=(dbvalue,displayvalue)
    mode_choices=(('offline','OFFLINE'),('online','ONLINE'))
    course_name=models.CharField(max_length=30)
    fee=models.IntegerField()
    duration=models.CharField(max_length=30)
    instructor=models.CharField(max_length=30)
    # mode=models.CharField(max_length=30)
    mode=models.CharField(choices=mode_choices)


