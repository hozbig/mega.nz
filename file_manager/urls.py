from django.urls import path
from .views import Dashboard, delete_file, save_files

app_name = 'file_manager'
urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('save/', save_files, name='save_files'),
    path('delete/<id>', delete_file, name='delete_file'),
]