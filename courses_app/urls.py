from django.urls import path
from .views import CoursesView

urlpatterns = [path("courses_app/", CoursesView.as_view(), name="courses_app")]
