from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .mixins import FormValidMixin
from .models import FileManager


# Create your views here.
class UploadFile(LoginRequiredMixin, FormValidMixin, SuccessMessageMixin, CreateView):
    model = FileManager
    template_name = 'file_manager/upload.html'
    fields = ['file', 'divide_to', 'size']

    login_url = 'account:login'

    success_message = 'Yay! Your file has been uploaded successfully.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["uploaded_files"] = FileManager.objects.filter(owner=self.request.user).order_by('-created_time')
        return context
    
