from django.urls import path
from TalentPoolWeb import views

app_name = "web"

urlpatterns = [
    path("", view=views.user_login),
    path("login/", view=views.user_login, name="login"),
    path("logout/", view=views.user_logout, name="logout"),
    path("register/", view=views.register, name="register"),
]
