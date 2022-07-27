from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets[1][1]['fields'] = (
    "first_name", "last_name", "email", "email_activation"
    )
UserAdmin.list_display = (
    "username", "email", "first_name", "last_name", "is_staff", "email_activation"
    )

admin.site.register(User, UserAdmin)