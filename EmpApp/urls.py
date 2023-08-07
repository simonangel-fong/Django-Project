from django.urls import path
from EmpApp import views

app_name = "EmpApp"

urlpatterns = [
    path("", view=views.emp_list, name="index"),
    path("emp/list/", view=views.emp_list, name="emp_list"),
    path("emp/add/", view=views.emp_add, name="emp_add"),
    path("emp/detail/<int:emp_id>", view=views.emp_detail, name="emp_detail"),
    path("emp/update/<int:emp_id>", view=views.emp_update, name="emp_update"),
    path("emp/delete/<int:emp_id>", view=views.emp_delete, name="emp_delete"),

    path("dept/list/", view=views.dept_list, name="dept_list"),
    path("dept/add/", view=views.dept_add, name="dept_add"),
    path("dept/detail/<int:dept_id>", view=views.dept_detail, name="dept_detail"),
    path("dept/update/<int:dept_id>", view=views.dept_update, name="dept_update"),
    path("dept/delete/<int:dept_id>", view=views.dept_delete, name="dept_delete"),

    path("register", view=views.register, name="register"),
]
