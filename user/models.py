from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.email = email
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")
        if extra_fields.get('is_active') is not True:
            raise ValueError("Superuser must have is_active=True")
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    USER_TYPES = (
        ('admin', 'ADMIN'),
    )

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField("Email Address", unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=USER_TYPES, blank=True, 
                            null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
