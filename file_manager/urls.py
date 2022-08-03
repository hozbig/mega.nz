from django.urls import path
from .views import UploadFile

app_name = 'file_manager'
urlpatterns = [
    path('', UploadFile.as_view(), name='upload'),
]