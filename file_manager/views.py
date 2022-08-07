from django.shortcuts import render
from django.views.generic.edit import CreateView

from .mixins import FormValidMixin
from .models import FileManager


# Create your views here.
class UploadFile(FormValidMixin, CreateView):
    model = FileManager
    template_name = 'file_manager/upload.html'
    fields = ['file', 'divide_to', 'size']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["uploaded_files"] = FileManager.objects.filter(owner=self.request.user)
        return context
    
