from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .mixins import FormValidMixin
from .models import FileManager


# Create your views here.
class UploadFile(FormValidMixin, SuccessMessageMixin, CreateView):
    model = FileManager
    template_name = 'file_manager/upload.html'
    fields = ['file', 'divide_to', 'size']

    success_message = 'upload_successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["uploaded_files"] = FileManager.objects.filter(owner=self.request.user).order_by('-created_time')
        return context
    
