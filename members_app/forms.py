from django import forms
from courses_app.models import Courses
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class StyledUserCreationForm(UserCreationForm):
    """Customized UserCreationForm with additional styling"""

    GENDERS = (("male", "Male"), ("female", "Female"))
    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    gender = forms.ChoiceField(choices=GENDERS, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "gender",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs[
            "class"
        ] = "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm"
        self.fields["last_name"].widget.attrs[
            "class"
        ] = "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm"
        self.fields["date_of_birth"].widget.attrs[
            "class"
        ] = "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm"
        self.fields["username"].widget.attrs[
            "class"
        ] = "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm"
        self.fields["password1"].widget.attrs[
            "class"
        ] = "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm"
        self.fields["password2"].widget.attrs[
            "class"
        ] = "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm"
        self.fields["email"].widget.attrs[
            "class"
        ] = "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm"


class StyledAuthenticationForm(AuthenticationForm):
    """Customized AuthenticationForm with additional styling"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs[
            "class"
        ] = "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm"
        self.fields["password"].widget.attrs[
            "class"
        ] = "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm"


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
