from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    email_activation = models.BooleanField(default=False)
    user_uploaded_volume = models.IntegerField(
        ("user uploaded volume(byte)"),
        default=0,
        blank=True,
    )
    premium = models.DateTimeField(default=timezone.now)

    def is_premium(self):
        if self.premium > timezone.now():
            return True
        else:
            return False
    is_premium.boolean = True
