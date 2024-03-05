from django import forms


class CourseForm(forms.Form):
    """Definition of a Django form class for handling course data."""

    title = forms.CharField(label="Title", required=True, max_length=255)
    title.widget.attrs.update(
        {
            "class": "pl-5 h-9 bg-transparent border border-gray-300 w-full rounded-md text-sm",
            "placeholder": "Title",
        }
    )
