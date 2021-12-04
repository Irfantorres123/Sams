from django.db import models

from schedule.models import Lecture
from user.models import Student


class AttendanceStatus(models.TextChoices):
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"


class Attendance(models.Model):
    """
    Stores attendance for every lecture
    """
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    status = models.CharField(choices=AttendanceStatus.choices)
