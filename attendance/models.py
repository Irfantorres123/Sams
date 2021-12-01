from django.db import models

from schedule.models import Lecture
from user.models import Student


class AttendanceState(models.TextChoices):
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"


class Attendance(models.Model):
    """
    Stores attendance for every lecture
    """
    lectureId = models.ForeignKey(Lecture, on_delete=models.DO_NOTHING)
    studentId = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendanceState = models.CharField(choices=AttendanceState.choices)
