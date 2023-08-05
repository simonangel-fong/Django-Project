from django.db import models


class Department(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name="Department's Name",
        unique=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="The address of this department",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "department"
        verbose_name = "The table storing department information."
        indexes = [
            models.Index(fields=["name"]),
        ]


class Employee(models.Model):
    first_name = models.CharField(
        max_length=64,
        verbose_name="The employess's first name"
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name="The employess's last name"
    )
    email = models.EmailField(
        max_length=255,
        verbose_name="The employess's email address",
        unique=True
    )
    dept = models.ForeignKey(
        Department,
        on_delete=models.SET_DEFAULT,
        verbose_name="The employess's department",
        null=True,
        default=None
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "employee"
        verbose_name = "The table storing employees information."
        indexes = [
            models.Index(fields=["last_name", "first_name"]),
            models.Index(fields=["email"]),
        ]
