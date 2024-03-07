from django.urls import path
from .views import (
    MembersView,
    SuccessView,
    HomeView,
    TodoView,
    TodoUpdateView,
    TodoDeleteView,
    MainView,
    UserEnrollmentView,
    UserEnrollmentDeleteView,
    UserEnrollmentUpdateView,
)


urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("members_app/", HomeView.as_view(), name="members_app"),
    path("members_app/login/", MembersView.as_view(), name="members_login"),
    path("members_app/success/", SuccessView.as_view(), name="members_success"),
    path("members_app/todo/", TodoView.as_view(), name="members_todo"),
    path(
        "members_app/todo/update/<str:todo_id>",
        TodoUpdateView.as_view(),
        name="members_todo_update",
    ),
    path(
        "members_app/todo/delete/<str:todo_id>",
        TodoDeleteView.as_view(),
        name="members_todo_delete",
    ),
    path(
        "members_app/user_enrollment/",
        UserEnrollmentView.as_view(),
        name="members_enrollment",
    ),
    path(
        "members_app/user_enrollment/delete/<str:enrollment_id>",
        UserEnrollmentDeleteView.as_view(),
        name="members_enrollment_delete",
    ),
    path(
        "members_app/user_enrollment/update/<str:enrollment_id>",
        UserEnrollmentUpdateView.as_view(),
        name="members_enrollment_update",
    ),
]
