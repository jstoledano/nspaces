# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-03 04:17
from __future__ import unicode_literals

from django.db import migrations
import draceditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170802_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=draceditor.models.DraceditorField(verbose_name='Contenido'),
        ),
    ]
