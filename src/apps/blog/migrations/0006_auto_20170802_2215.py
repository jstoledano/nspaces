# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-03 03:15
from __future__ import unicode_literals

from django.db import migrations
import draceditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170802_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='extend',
            field=draceditor.models.DraceditorField(blank=True, verbose_name='Extendido'),
        ),
    ]
