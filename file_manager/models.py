from account.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from pathlib import Path


class FMManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-created_time')


class FileManager(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="files/")
    format = models.CharField(max_length=50, blank= True)
    size = models.CharField(('size(bytes)'), max_length=50, blank= True)

    divide_to = models.IntegerField(
        validators=[MinValueValidator(3)],
        default=3,
    )

    created_time = models.DateTimeField(auto_now_add=True, blank=True)

    objects = FMManager()

    def __str__(self):
        return f'{self.file} - {self.format} - {self.size}'

    def get_absolute_url(self):
        return reverse("file_manager:upload")



def get_format(sender, instance, *args, **kwargs):
    instance.format = Path(str(instance.file)).suffix

pre_save.connect(get_format, sender=FileManager)