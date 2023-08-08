from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from TalentPoolWeb.models import UserProfile
from TalentPoolWeb.forms import ProfileForm, UserForm


def home(request):
    ''' Home page '''
    template = "TalentPoolWeb/index.html"
    context = {
        "title": "Home",
        "heading": "Talent Pool",
    }
    return render(request, template, context)


def user_login(request):
    ''' User login page '''
    template = "TalentPoolWeb/login.html"
    context = {
        "title": "Login",
        "heading": "Login"
    }
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            context["error_message"] = "User Name or Password is invalid."

    return render(request, template, context)


def user_logout(request):
    ''' Logout page '''

    logout(request)
    return redirect("web:login")


def register(request):
    ''' Register page '''

    userForm = UserForm()
    profileForm = ProfileForm()

    if request.method == "POST":
        userForm = UserForm(data=request.POST)
        profileForm = ProfileForm(data=request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            print("form valid")
            newUser = userForm.save(commit=False)
            newUser.set_password(newUser.password)
            newUser.save()

            newProfile = profileForm.save(commit=False)
            newProfile = newUser
            if "profile_img" in request.FILES:
                newProfile.profile_img = request.FILES["profile_img"]
            newProfile.save()
            return redirect("web:login")

    template = "TalentPoolWeb/register.html"
    context = {
        "title": "Register",
        "heading": "Register",
        "userForm": userForm,
        "profileForm": profileForm
    }

    return render(request, template, context)
