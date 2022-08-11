from django.forms import ModelForm
from .models import FileManager

class FileManagerForm(ModelForm):
    class Meta:
        model = FileManager
        fields = ['file', 'size', 'divide_to']