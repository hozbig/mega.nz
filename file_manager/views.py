from account.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic.list import ListView

from .forms import FileManagerForm
from .models import FileManager


class Dashboard(LoginRequiredMixin, ListView):
    model = FileManager
    template_name = 'file_manager/dashboard.html'

    login_url = 'account:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FileManagerForm()
        return context

@login_required
def save_files(request):
    if request.method == 'POST':
        user = request.user
        if user.user_uploaded_volume <= user.user_level.max_upload_file or user.premium:
            form = FileManagerForm(request.POST or None, request.FILES or None)
            files = request.FILES.getlist('file')
            file_divide_to = request.POST['divide_to']
            file_size = str(request.POST['size']).split(',')
            if form.is_valid():
                if files:
                    for idx, f in enumerate(files):
                        FileManager.objects.create(
                            owner=user,
                            file=f,
                            size=file_size[idx],
                            divide_to=file_divide_to
                        )
                        user.user_uploaded_volume += int(file_size[idx])
                        user.save()

                messages.success(
                    request, 'Yay! Your file(s) has been uploaded successfully.')
                return redirect('file_manager:dashboard')
        else:
            raise Http404("Access Denide!")
    else:
        return redirect('file_manager:dashboard')


@login_required
def delete_file(request, id):
    file = FileManager.objects.get(id=id)
    user = request.user
    user.user_uploaded_volume -= int(file.size)
    file.delete()
    user.save()
    messages.success(
                    request, 'Your file deleted successfully.')
    return redirect('file_manager:dashboard')
