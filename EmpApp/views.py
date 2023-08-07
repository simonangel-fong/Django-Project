from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Employee, Department
from .forms import EmpForm, DeptForm, UserProfileForm, UserForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

# region project view


def index(request):
    ''' Home page '''
    context = {
        'title': 'Home',
        "main_title": "Employee App.",
    }
    template = "index.html"
    return render(request, template, context)


def success(request, msg):
    ''' Success Page '''
    template = "success.html"
    context = {
        "title": "Success",
        "main_title": "Success",
        "msg": msg.replace("-", " ")
    }
    return render(request, template, context)
# endregion

# region Department View


def dept_list(request):
    '''Departments List Page'''
    template = 'EmpApp/dept_list.html'
    dept_list = Department.objects.all()
    context = {
        "title": "Department List",
        "main_title": "Department List",
        "data": dept_list}
    return render(request, template, context)


def dept_detail(request, dept_id):
    '''Department Detail Page'''
    dept = get_object_or_404(Department, pk=dept_id)
    template = "EmpApp/dept_detail.html"
    context = {
        "title": f'Department: {dept.name}',
        "main_title": "Department Detail",
        "data": dept
    }
    return render(request, template, context)


def dept_add(request):
    '''Department Add Page'''
    form = DeptForm()
    template = 'EmpApp/dept_add.html'

    if request.method == "POST":
        form = DeptForm(request.POST)

        if form.is_valid():
            newDept = form.save()
            msg = f"Add a department data: {newDept}"
            print(f"{datetime.now()}: {msg}")
            return redirect("success", msg=slugify(msg))

    context = {
        "title": "Add new Department",
        "main_title": "Add new Department",
        "form": form
    }

    return render(request, template, context)


def dept_update(request, dept_id):
    '''Department Update Page'''
    dept = get_object_or_404(Department, pk=dept_id)

    if request.method == "POST":
        form = DeptForm(request.POST, instance=dept)
        if form.is_valid():
            newDept = form.save()
            msg = f"Update department data: {newDept}"
            print(f"{datetime.now()}: {msg}")
            return redirect("success", msg=slugify(msg))

    form = DeptForm(instance=dept)
    template = 'EmpApp/dept_add.html'
    context = {
        "title": "Update Department",
        "main_title": "Update Department",
        "form": form
    }

    return render(request, template, context)


def dept_delete(request, dept_id):
    '''Department Update Page'''
    if request.method == "POST":
        dept = get_object_or_404(Department, pk=dept_id)
        del_dept = dept.delete()
        msg = f"Delete department record: {dept}"
        print(f"{datetime.now()} {msg}")
        return redirect("success", msg=slugify(msg))
    return redirect("index")
# endregion

# region Employee View


def emp_list(request):
    '''Employee List Page'''
    template = 'EmpApp/emp_list.html'
    emp_list = Employee.objects.all()
    context = {
        "title": "Employee List",
        "main_title": "Employee List",
        "data": emp_list}
    return render(request, template, context)


def emp_detail(request, emp_id):
    '''Employee Detail Page'''
    emp = get_object_or_404(Employee, pk=emp_id)
    template = "EmpApp/emp_detail.html"
    context = {
        "title": f'Department: {emp}',
        "main_title": "Employee Detail",
        "data": emp
    }
    return render(request, template, context)


def emp_add(request):
    '''Department Add Page'''
    form = EmpForm()
    template = 'EmpApp/emp_add.html'

    if request.method == "POST":
        form = EmpForm(request.POST)

        if form.is_valid():
            newDept = form.save()
            msg = f"Add a employee data: {newDept}"
            print(f"{datetime.now()}: {msg}")
            return redirect("success", msg=slugify(msg))

    context = {
        "title": "Add new Employee",
        "main_title": "Add new Employee",
        "form": form
    }

    return render(request, template, context)


def emp_update(request, emp_id):
    '''Employee UPdate Page'''
    emp = get_object_or_404(Employee, pk=emp_id)

    if request.method == "POST":
        form = EmpForm(request.POST, instance=emp)
        if form.is_valid():
            newEmp = form.save()
            msg = f"Update employee record: {newEmp}"
            print(f"{datetime.now()} {msg}")
            return redirect("success", msg=slugify(msg))

    form = EmpForm(instance=emp)
    template = "EmpApp/emp_add.html"
    context = {
        "title": "Update Employee",
        "main_title": "Update Employee",
        "form": form
    }

    return render(request, template, context)


def emp_delete(request, emp_id):
    '''Employee Delete Page'''
    if request.method == "POST":
        emp = get_object_or_404(Employee, pk=emp_id)
        del_emp = emp.delete()
        msg = f"Delete employee record: {emp}"
        print(f"{datetime.now()} {msg}")
        return redirect("success", msg=slugify(msg))
    return redirect()
# endregion


# region user profile info

def register(request):
    ''' user info '''
    userForm = UserForm()
    profileForm = UserProfileForm()
    if request.method == "POST":
        userForm = UserForm(data=request.POST)
        profileForm = UserProfileForm(data=request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            newUser = userForm.save(commit=False)
            newUser.set_password(request.POST["password"])
            newUser.save()

            new_profile = profileForm.save(commit=False)
            new_profile.user = newUser
            if "profile_pic" in request.FILES:
                new_profile.profile_pic = request.FILES["profile_pic"]

            new_profile.save()
            msg = f"Create User: {newUser}"
            print(f"{datetime.now()} {msg}")
            return redirect("success", msg=slugify(msg))
        else:
            print(userForm.errors)
    template = "register.html"

    context = {
        "userForm": userForm,
        "profileForm": profileForm
    }
    return render(request, template, context)

# endregion
