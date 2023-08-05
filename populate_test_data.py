
import django
import os
import random
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmployeeProject.settings')

django.setup()
from EmpApp.models import Employee, Department


def populate_dept_data(arr):
    for dept in arr:
        fake = Faker()
        address = fake.profile()["address"]
        newDept = Department.objects.get_or_create(
            name=dept,
            address=address
        )
    print(f"Insert {len(arr)} department records.")


def populate_emp_data(num=10):
    dept_list = Department.objects.all()
    faker = Faker()
    Faker.seed(42)

    for _ in range(num):
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.profile()["mail"]
        dept = random.choice(dept_list)
        newEmp = Employee.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            dept=dept
        )
    print(f"Insert {num} department records.")


def clear_data():
    del_dept = Department.objects.all().delete()
    print("Delete {} rows of Department data.".format(del_dept[0]))

    del_emp = Employee.objects.all().delete()
    print("Delete {} rows of Employee data.\n".format(del_emp[0]))


def get_size():
    size = Employee.objects.all().count()
    return size


if __name__ == "__main__":
    print("\n-------- Task: Populates testing data --------\n")
    clear_data()
    dept_arr = [
        "research & development",
        "manufacturing",
        "maintenance",
        "quality conttol",
        "sales",
        "marketing",
        "finance",
        "it",
        "personnel",
        "not applicable",
    ]
    populate_dept_data(dept_arr)
    populate_emp_data(100)
    print("\n-------- Task completed. --------\n")
