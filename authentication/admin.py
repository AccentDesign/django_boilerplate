from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.sessions.models import Session

from authentication.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Personal info', {'fields': ('first_name', 'last_name', )}),
        ('Important dates', {'fields': ('last_login', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', )}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', )}),
        ('Personal info', {'fields': ('first_name', 'last_name', )}),
    )
    search_fields = ('email', )
    ordering = ('email', )


admin.site.register(Session)
admin.site.register(User, UserAdmin)
