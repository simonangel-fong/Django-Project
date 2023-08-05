from django.contrib import admin
from .models import Employee,Department

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)

admin.site.site_header = "Employee Management Admin"
admin.site.site_title = "Employee Management Admin"