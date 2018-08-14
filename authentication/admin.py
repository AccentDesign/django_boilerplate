from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.sessions.models import Session

from authentication.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_staff', )
    list_filter = ('is_staff', 'groups', )
    fieldsets = (
        (None, {'fields': ('email', )}),
        ('Personal info', {'fields': ('first_name', 'last_name', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', )}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', )}),
        ('Personal info', {'fields': ('first_name', 'last_name', )}),
    )
    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ('groups', )


admin.site.register(Session)
admin.site.register(User, UserAdmin)
