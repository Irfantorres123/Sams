from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserMeta(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class StudentMeta(UserMeta):
    pass


class TeacherMeta(UserMeta):
    pass


class Student(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    dataId = models.ForeignKey(StudentMeta, on_delete=models.PROTECT)


class Teacher(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    dataId = models.ForeignKey(TeacherMeta, on_delete=models.PROTECT)
