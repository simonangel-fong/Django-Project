from django import forms
from .models import Employee, Department
from django.utils.translation import gettext_lazy as _


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
