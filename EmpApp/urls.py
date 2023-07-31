from django.urls import path
from EmpApp import views

urlpatterns = [
    path("", view=views.index, name="index")
]
