# coding: utf-8

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
