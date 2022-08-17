from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Level

UserAdmin.fieldsets[1][1]['fields'] = (
    "first_name", "last_name", "email", "email_activation"
)
UserAdmin.fieldsets[2][1]['fields'] = (
    "is_active",
    "premium",
    "user_level",
    "is_staff",
    "is_superuser",
    "groups",
    "user_permissions",
)
UserAdmin.fieldsets += (
    ("Volume manager", {"fields": ("user_uploaded_volume", )}),
)
UserAdmin.list_display = (
    "username", "email", "first_name", "last_name", "is_staff", "email_activation"
)

admin.site.register(User, UserAdmin)

admin.site.register(Level)