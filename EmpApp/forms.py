from django import forms
from EmpApp.models import Employee, Department, UserProfile
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        labels = {
            "first_name": _("First Name"),
            "last_name": _("Last Name"),
            "email": _("Email"),
            "dept": _("Department"),
        }
        error_messages = {
            "first_name": {
                "max_length": _("Accept less than 64 characters."),
                "required": _("First name cannot be empty."),
            },
            "last_name": {
                "max_length": _("Accept less than 64 characters."),
            },
            "email": {
                "max_length": _("Accept less than 255 characters."),
                "validate_email": _("Must be a valid email."),
            },
        }
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control"
            }),
            "dept": forms.Select(attrs={
                "class": "form-select",
                "default": "aa"
            }),
        }


class DeptForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        labels = {
            "name": _("Department Name"),
            "address": _("Address"),
        }
        error_messages = {
            "name": {
                "max_length": _("Accept less than 64 characters."),
                "required": _("First name cannot be empty."),
            },
            "address": {
                "max_length": _("Accept less than 64 characters."),
            },
        }


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ("username", "email", "password")
        labels = {
            "username": _("User Name"),
            "email": _("Email"),
            "password": _("Password")
        }
        widgets = {
            "username": forms.TextInput(attrs={
                "max_length": 60,
                "class": "form-control",
            }),
            "email": forms.EmailInput(attrs={
                "max_length": 60,
                "class": "form-control",
            }),
            "password": forms.PasswordInput(attrs={
                "max_length": 60,
                "class": "form-control",
            }),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("portfolio_site", "profile_pic",)
