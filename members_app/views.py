from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import (
    StyledUserCreationForm,
    StyledAuthenticationForm,
    TodoForm,
    UserEnrollmentForm,
)
from uuid import uuid4
from .models import UserEnrollments
from django.contrib.auth import login, logout


class MainView(View):
    # Class-based view for rendering the main page.

    def get(self, request):
        return render(request, "home.html", {"title": "Main"})


class HomeView(View):
    def get(self, request):
        # Render the 'home.html' template with the title "Home".

        return render(request, "members.html", {"title": "Members"})


class RegistrationView(View):
    # Class-based view for handling member registration.

    # Template name for rendering the registration form.
    template_name = "registration.html"

    # Form class to handle registration inputs.
    form = StyledUserCreationForm

    def get(self, request):
        # Handles GET requests to display the registration form.

        # Render the 'registration.html' template with the UserCreationForm and title.
        return render(
            request, self.template_name, {"form": self.form, "title": "Registration"}
        )

    def post(self, request):
        # Handles POST requests to process form submission.

        # Instantiate the StyledUserCreationForm with POST data.
        form = self.form(request.POST)

        # If the form is valid, get the user associated with the form
        if form.is_valid():
            user = form.save()

            # Log in the user using Django's login function
            login(request, user)

            # Redirect the user to the home page after successful login
            return HttpResponseRedirect("/")

        # If form is not valid, render the 'registration.html' template with the form and title.
        return render(
            request, self.template_name, {"form": form, "title": "Registration"}
        )


class LoginView(View):
    # Class-based view for handling member login.

    # Template name for rendering the login form.
    template_name = "login.html"

    # Form class to handle login inputs.
    form = StyledAuthenticationForm

    def get(self, request):
        # Handles GET requests to display the login form.

        # Render the 'login.html' template with the StyledAuthenticationForm and title.
        return render(
            request, self.template_name, {"form": self.form, "title": "Login"}
        )

    def post(self, request):
        # Handles POST requests to process form submission.

        # Instantiate the StyledAuthenticationForm with POST data.
        form = self.form(request, data=request.POST)

        # If the form is valid, get the user associated with the form
        if form.is_valid():
            user = form.get_user()

            # Log in the user using Django's login function
            login(request, user)

            # Redirect the user to the home page after successful login
            return HttpResponseRedirect("/")

        # If form is not valid, render the 'login.html' template with the form and title.
        return render(request, self.template_name, {"form": form, "title": "Login"})


class LogoutView(View):
    # Class-based view for handling user logout
    def post(_, request):
        # Log the user out using Django's logout function
        logout(request)

        # Redirect the user to the home page after logout
        return HttpResponseRedirect("/")


class TodoView(View):
    # Class-based view for managing a todo list.

    # Template name for rendering the todo list.
    template_name = "todo_list.html"

    # Form class to handle todo input.
    form = TodoForm

    def get(self, request):
        # Handles GET requests to display the todo list.

        # Retrieve the todo list from the session or create an empty list if not present.
        todo_list = request.session.get("todo_list", [])

        # Render the 'todo_list.html' template with the TodoForm, todo list, and title.
        return render(
            request,
            self.template_name,
            {"form": self.form, "todo_list": todo_list, "title": "Todo list"},
        )

    def post(self, request):
        # Handles POST requests to process todo form submissions.

        # Instantiate the TodoForm with POST data.
        form = self.form(request.POST)

        # Retrieve the current todo list from the session or create an empty list if not present.
        todo_list = request.session.get("todo_list", [])

        # If form is valid, append the new todo item to the list and update the session.
        if form.is_valid():
            todo_list.append(
                {
                    "title": form.cleaned_data["title"],
                    "checked": False,
                    "id": str(uuid4()),
                }
            )
            request.session["todo_list"] = todo_list

        # Render the 'todo_list.html' template with the updated TodoForm, todo list, and title.
        return render(
            request,
            self.template_name,
            {"form": self.form, "todo_list": todo_list, "title": "Todo list"},
        )


class TodoUpdateView(View):
    def get(self, request, todo_id):
        # Handles GET requests to update the status of a todo item.

        # Retrieve the current todo list from the session or create an empty list if not present.
        todo_list = request.session.get("todo_list", [])

        # Update the checked status of the todo item with the specified todo_id.
        updated_todo_list = [
            {**t, "checked": not t["checked"]} if t["id"] == todo_id else t
            for t in todo_list
        ]

        # Update the session with the modified todo list.
        request.session["todo_list"] = updated_todo_list

        # Redirect to the todo list page after updating the todo item.
        return HttpResponseRedirect("/members_app/todo/")


class TodoDeleteView(View):
    def get(self, request, todo_id):
        # Handles GET requests to delete a todo item.

        # Retrieve the current todo list from the session or create an empty list if not present.
        todo_list = request.session.get("todo_list", [])

        # Filter out the todo item with the specified todo_id from the todo list.
        updated_todo_list = [t for t in todo_list if t["id"] != todo_id]

        # Update the session with the modified todo list.
        request.session["todo_list"] = updated_todo_list

        # Redirect to the todo list page after deleting the todo item.
        return HttpResponseRedirect("/members_app/todo/")


class UserEnrollmentView(View):
    # Class-based view for managing a user enrollment list.

    # Template name for rendering the user enrollment list.
    template_name = "enrollment.html"

    # Form class to handle user enrollment inputs.
    form = UserEnrollmentForm

    def get(self, request):
        # Handles GET requests to display the user enrollment list.

        # Retrieve all user enrollments from the database.
        user_enrollments = UserEnrollments.objects.all()

        # If a enrollment_id is provided in the query parameters, prepopulate the form.
        if request.GET.get("enrollment_id"):
            user_enrollment = user_enrollments.filter(
                id=request.GET.get("enrollment_id")
            ).first()
            initial_values = {
                "user": user_enrollment.user,
                "course": user_enrollment.course,
            }
            self.form = UserEnrollmentForm(initial=initial_values)

        # Render the template with the form and user enrollments data.
        return render(
            request,
            self.template_name,
            {
                "title": "Enrollment",
                "form": self.form,
                "user_enrollments": user_enrollments,
            },
        )

    def post(self, request):
        # Handles POST requests to process user enrollments form submissions.

        # Instantiate the UserEnrollmentForm with POST data.
        form = self.form(request.POST)

        # If the form is valid, create a new user enrollment in the database.
        if form.is_valid():
            user = form.cleaned_data["user"]
            course = form.cleaned_data["course"]
            UserEnrollments.objects.create(user=user, course=course)

        # Redirect to the user enrollments page after processing the form.
        return HttpResponseRedirect("/members_app/user_enrollment/")


class UserEnrollmentDeleteView(View):
    # Class-based view for deleting a user enrolment.

    def get(self, _, enrollment_id):
        # Handles GET requests to delete a user enrollment item.

        # Delete the user enrollment with the specified enrollment_id.
        UserEnrollments.objects.get(id=enrollment_id).delete()

        # Redirect to the user enrollments page after deleting the enrollment.
        return HttpResponseRedirect("/members_app/user_enrollment/")


class UserEnrollmentUpdateView(View):
    # Handles POST requests to update the user enrollment item.

    def post(self, request, enrollment_id):

        # Create a form instance with the POST data.
        form = UserEnrollmentForm(request.POST)

        # If the form is valid, update the user enrollment in the database.
        if form.is_valid():
            user = form.cleaned_data["user"]
            course = form.cleaned_data["course"]
            UserEnrollments.objects.filter(id=enrollment_id).update(
                user=user, course=course
            )

            # Redirect to the user enrollments page after updating the course.
            return HttpResponseRedirect("/members_app/user_enrollment/")
