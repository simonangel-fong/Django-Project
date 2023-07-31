from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self) -> str:
        return "{0} {1}".format(self.first_name, self.last_name)
