from django.db import models
from django.db.models import indexes

from university.models import SemesterCourse


class Days(models.TextChoices):
    SUN = "SUNDAY"
    MON = "MONDAY"
    TUE = "TUESDAY"
    WED = "WEDNESDAY"
    THU = "THURSDAY"
    FRI = "FRIDAY"
    SAT = "SATURDAY"


class Lecture(models.Model):
    """
    One-to-many mapping of semester course to day and time. 
    You could say this contains lectures cause teaching of a course on a particular day at a particular time is what a lecture is.
    Tells us the various times when this course is taught
    This does not impose a strict limit however, and is only for the app to suggest courses.
    It should still be possible to teach a different course during a time allocated to this course.
    """
    sCourseId = models.ForeignKey(SemesterCourse, on_delete=models.DO_NOTHING)

    day = models.CharField(choices=Days.choices, blank=False, null=False)
    startTime = models.TimeField()
    endTime = models.TimeField()
    indexes = [models.Index(fields=['sCourseId'])]
