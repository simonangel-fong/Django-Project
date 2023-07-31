from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee


def index(request):
    empList = Employee.objects.all()
    context = {"data": empList}
    return render(request, 'index.html', context)
