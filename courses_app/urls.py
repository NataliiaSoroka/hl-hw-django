from django.urls import path
from .views import CoursesView, CourseDeleteView, CourseUpdateView

urlpatterns = [
    path("courses_app/", CoursesView.as_view(), name="courses_app"),
    path(
        "courses_app/delete/<str:course_id>",
        CourseDeleteView.as_view(),
        name="courses_delete",
    ),
    path(
        "courses_app/update/<str:course_id>",
        CourseUpdateView.as_view(),
        name="courses_update",
    ),
]
