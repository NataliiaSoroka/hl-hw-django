from django import forms


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
