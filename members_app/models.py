from django.db import models
from django.contrib.auth.models import User
from courses_app.models import Courses


class UserEnrollments(models.Model):
    """Model for representing user enrollments in courses."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.name} on {self.enrollment_date}"
