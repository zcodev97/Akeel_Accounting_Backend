from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username", "password1", "password2",
                    "email", "first_name", "last_name"),
            },
        ),
    )
    list_display = ['id', 'username', 'first_name',
                    'last_name', 'email', 'is_superuser']
