from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email_activation = models.BooleanField(default=False)
    user_uploaded_volume = models.IntegerField(
        ("user uploaded volume(byte)"),
        default=0,
        blank=True,
    )
