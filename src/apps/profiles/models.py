# coding: utf-8

import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from authtools.models import AbstractNamedUser


class User(AbstractNamedUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.email


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
