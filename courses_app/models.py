from django.db import models


class Courses(models.Model):
    """Model definition for representing courses."""

    title = models.CharField(max_length=255)
    enrollments = models.ManyToManyField("members_app.UserEnrollments")

    def __str__(self):
        return self.title
