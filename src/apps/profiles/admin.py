# coding: utf-8
from django.contrib import admin
from authtools.admin import NamedUserAdmin
from apps.profiles.models import User


class UserAdmin(NamedUserAdmin):
    pass

admin.site.register(User, UserAdmin)
