# coding: utf-8

import uuid
from django.db import models
from authtools.models import AbstractNamedUser


class User(AbstractNamedUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
