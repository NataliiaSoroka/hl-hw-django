from django.shortcuts import render
from django.views import View


class CoursesView(View):
    def get(self, request):
        """Render the 'courses.html' template with the title "Courses" and the current user information."""

        return render(
            request, "courses.html", {"title": "Courses", "user": request.user}
        )
