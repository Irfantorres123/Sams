from django.db import models
from university.validators import *
from user.models import Student, Teacher
# Create your models here.


class University(models.Model):
    """
    University model
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    Contains Department information
    Every entry here belongs to a particular university which is what the uid foreign key is for
    """
    name = models.CharField(max_length=255)
    uid = models.ForeignKey(University, on_delete=models.DO_NOTHING)


class Course(models.Model):
    """
    Every course belongs to a certain department in a certain university and has a course code
    """
    name = models.CharField(max_length=255, null=False, blank=True)
    uid = models.ForeignKey(
        University, on_delete=models.DO_NOTHING, null=False, blank=False)
    departmentId = models.ForeignKey(
        Department, on_delete=models.DO_NOTHING, null=False, blank=False)
    code = models.CharField(max_length=20, null=False, blank=False)


class SemesterCourse(models.Model):
    """
    This represents the state of a course during a particular semester since the same course
    will be taught repeatedly. Year and month mark the beginning of the course
    """
    courseId = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    year = models.SmallIntegerField()
    month = models.ChoiceField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


class StudentCourse(models.Model):
    """
    One-to-many mapping of student to semester courses. 
    Tells us what courses a student is enrolled in.
    semesterNumber is the sem when the student takes up that course
    """
    studentId = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    sCourseId = models.ForeignKey(SemesterCourse, on_delete=models.DO_NOTHING)
    semesterNumber = models.PositiveSmallIntegerField()


class TeacherCourse(models.Model):
    """
    One-to-Many mapping of teacher to semester courses. 
    Tells what courses a teacher is teaching every semester.
    """
    teacherId = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    sCourseId = models.ForeignKey(SemesterCourse, on_delete=models.DO_NOTHING)
