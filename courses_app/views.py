from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import CourseForm
from .models import Courses


class CoursesView(View):
    # Class-based view for managing a course list.

    # Template name for rendering the course list.
    template_name = "courses.html"

    # Form class to handle course input.
    form = CourseForm

    def get(self, request):
        # Handles GET requests to display the course list.

        # Retrieve all courses from the database.
        courses = Courses.objects.all()

        # If a course_id is provided in the query parameters, prepopulate the form.
        if request.GET.get("course_id"):
            initial_values = {
                "title": courses.filter(id=request.GET.get("course_id")).first()
            }
            self.form = CourseForm(initial=initial_values)

        # Render the template with the form and courses data.
        return render(
            request,
            self.template_name,
            {"title": "Courses", "form": self.form, "courses": courses},
        )

    def post(self, request):
        # Handles POST requests to process course form submissions.

        # Instantiate the CourseForm with POST data.
        form = self.form(request.POST)

        # If the form is valid, create a new course in the database.
        if form.is_valid():
            title = form.cleaned_data["title"]
            Courses.objects.create(title=title)

        # Redirect to the courses page after processing the form.
        return HttpResponseRedirect("/courses_app/")


class CourseDeleteView(View):
    def get(self, _, course_id):
        # Handles GET requests to delete a course item.

        # Delete the course with the specified course_id.
        Courses.objects.get(id=course_id).delete()

        # Redirect to the courses page after deleting the course.
        return HttpResponseRedirect("/courses_app/")


class CourseUpdateView(View):
    # Handles POST requests to update the course item.

    def post(self, request, course_id):

        # Create a form instance with the POST data.
        form = CourseForm(request.POST)

        # If the form is valid, update the course in the database.
        if form.is_valid():
            title = form.cleaned_data["title"]
            Courses.objects.filter(id=course_id).update(title=title)

            # Redirect to the courses page after updating the course.
            return HttpResponseRedirect("/courses_app/")
