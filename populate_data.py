import django
import os
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmployeeProject.settings')

django.setup()

from EmpApp.models import Employee

def populate_emp_data(num=10):
    faker = Faker()
    Faker.seed(42)

    for _ in range(num):
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.profile()["mail"]
        newEmp = Employee.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        # print("Insert new data {}".format(newEmp))


def clear_data():
    del_info = Employee.objects.all().delete()
    print("Delete {} rows data.\n".format(del_info[0]))


def get_size():
    size = Employee.objects.all().count()
    return size


if __name__ == "__main__":
    print("\n-------- Populating data ... --------\n")
    clear_data()
    populate_emp_data(20)
    print("Successful insert {} rows.".format(get_size()))
    print("\n-------- Population ends. --------\n")
