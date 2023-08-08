from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password",)
        labels = {
            "username": _("User Name"),
            "password": _("Password"),
        }
        widgets = {
            "username": forms.TextInput(attrs={"max-length": 150, "class": "form-control"}),
            "password": forms.PasswordInput(attrs={"max-length": 150, "class": "form-control"}),
        }
