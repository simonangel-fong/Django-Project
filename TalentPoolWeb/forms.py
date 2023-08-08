from django.forms import ModelForm
from .models import UserProfile
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("username","password",)

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ("profile_img",)

