from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=10,
        choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')]
    )

    def __str__(self):
        return self.user.username
