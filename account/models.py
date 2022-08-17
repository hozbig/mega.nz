from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Level(models.Model):
    name = models.CharField(max_length=3)
    max_upload = models.PositiveIntegerField(default=2147483648)
    max_upload_file = models.PositiveIntegerField(default=1073741824)
    max_divide = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email_activation = models.BooleanField(default=False)
    user_uploaded_volume = models.IntegerField(
        ("user uploaded volume(byte)"),
        default=0,
        blank=True,
    )
    premium = models.DateTimeField(default=timezone.now)
    user_level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)

    def is_premium(self):
        if self.premium > timezone.now():
            return True
        else:
            return False
    is_premium.boolean = True
