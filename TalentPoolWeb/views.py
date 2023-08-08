from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from TalentPoolWeb.forms import UserForm


def home(request):
    ''' Home page '''
    context = {
        "title": "Home",
        "heading": "Talent Pool",
    }
    template = "TalentPoolWeb/index.html"
    return render(request, template, context)


def user_login(request):
    ''' User login page '''

    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            context["error_message"] = "User Name or Password is invalid."
    context["title"] = "Login"
    context["heading"] = "Login"
    template = "TalentPoolWeb/login.html"

    return render(request, template, context)


def user_logout(request):
    ''' Logout page '''

    logout(request)
    return redirect("web:login")


def register(request):
    ''' Register page '''
    context = {}
    if request.method == "POST":
        userForm = UserForm(data=request.POST)

        if userForm.is_valid():
            print("form valid")
            newUser = userForm.save(commit=False)
            newUser.set_password(newUser.password)
            newUser.save()
            return redirect("web:login")
        else:
            context["error_message"] = userForm.errors.as_text
    context["title"] = "Register"
    context["heading"] = "Register"
    context["userForm"] = UserForm()
    template = "TalentPoolWeb/register.html"

    return render(request, template, context)
