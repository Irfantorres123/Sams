from django.db import models

# Create your models here.

class University(models.Model):
    """
    University model
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name