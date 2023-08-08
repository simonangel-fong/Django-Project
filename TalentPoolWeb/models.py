from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    tel = models.CharField(
        max_length=20,
        blank=True
    )
    profile_img = models.ImageField(
        upload_to="profile_img",
        blank=True
    )

    def __str__(self):
        return self.user.username


# class OrganizationUser(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE
#     )
#     organ_name = models.CharField(
#         max_length=150
#     )
