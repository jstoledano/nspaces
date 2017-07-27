# coding: utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from apps.users.forms import CustomUserChangeForm, CustomUserCreationForm
from apps.users.models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
