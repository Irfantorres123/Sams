from django.db import models
from user.models import Student, Teacher
# Create your models here.
import calendar


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
    university = models.ForeignKey(University, on_delete=models.PROTECT)


class Course(models.Model):
    """
    Every course belongs to a certain department in a certain university and has a course code
    """
    name = models.CharField(max_length=255, null=False, blank=True)
    university = models.ForeignKey(
        University, on_delete=models.PROTECT, null=False, blank=False)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, null=False, blank=False)
    code = models.CharField(max_length=20, null=False, blank=False)


class SemesterCourse(models.Model):
    """
    This represents the state of a course during a particular semester since the same course
    will be taught repeatedly. Year and month mark the beginning of the course
    """
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    year = models.SmallIntegerField()
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]

    month = models.CharField(
        max_length=9, choices=MONTH_CHOICES, null=False, blank=False)


class StudentCourse(models.Model):
    """
    One-to-many mapping of student to semester courses. 
    Tells us what courses a student is enrolled in.
    semesterNumber is the sem when the student takes up that course
    """
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(SemesterCourse, on_delete=models.PROTECT)
    semesterNumber = models.PositiveSmallIntegerField()


class TeacherCourse(models.Model):
    """
    One-to-Many mapping of teacher to semester courses. 
    Tells what courses a teacher is teaching every semester.
    """
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    course = models.ForeignKey(SemesterCourse, on_delete=models.PROTECT)
