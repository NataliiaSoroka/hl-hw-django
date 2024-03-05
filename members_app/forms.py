from django import forms
from django.contrib.auth.models import User
from courses_app.models import Courses


class WelcomeForm(forms.Form):
    """A form for user greeting"""

    username = forms.CharField(label="Name", required=True, max_length=20)
    username.widget.attrs.update(
        {
            "class": "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm",
            "placeholder": "Your name",
        }
    )


class TodoForm(forms.Form):
    """A form for creating todo item"""

    title = forms.CharField(label="Title", required=True, min_length=20)
    title.widget.attrs.update(
        {
            "class": "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm"
        }
    )


class UserEnrollmentForm(forms.Form):
    """A form for creating user enrollment"""

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label=None,
        widget=forms.Select(
            attrs={
                "class": "h-8 pl-2.5 pr-2 rounded-md w-full shadow text-gray-700 border border-gray-200 leading-none py-0"
            }
        ),
    )
    course = forms.ModelChoiceField(
        queryset=Courses.objects.all(),
        empty_label=None,
        widget=forms.Select(
            attrs={
                "class": "h-8 pl-2.5 pr-2 rounded-md w-full shadow text-gray-700 border border-gray-200 leading-none py-0"
            }
        ),
    )
