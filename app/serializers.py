
from django.db import models
from app.models import Student
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    Name=serializers.CharField(max_length=30)
    Age=serializers.IntegerField()
    Course=serializers.CharField(max_length=30)
    Marks=serializers.IntegerField()
    def create(self,validated_data):
        e=Student.objects.create(**validated_data)
        return e


# class Course(models.Model):
#     # choices=(dbvalue,displayvalue)
#     mode_choices=(('offline','OFFLINE'),('online','ONLINE'))
#     course_name=models.CharField(max_length=30)
#     fee=models.IntegerField()
#     duration=models.CharField(max_length=30)
#     instructor=models.CharField(max_length=30)
#     # mode=models.CharField(max_length=30)
#     mode=models.CharField(choices=mode_choices)