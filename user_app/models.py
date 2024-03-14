from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Model for representing custom user."""

    GENDERS = (("male", "Male"), ("female", "Female"))
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(null=True, choices=GENDERS)

    def __str__(self):
        return self.username
