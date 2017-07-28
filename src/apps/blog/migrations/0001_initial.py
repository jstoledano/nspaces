# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 13:41
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Máximo 250 caracteres', max_length=250, verbose_name='Título')),
                ('slug', models.SlugField(help_text='Se sugiere el texto generado por el título. Debe ser único.', max_length=60, unique=True)),
                ('description', models.TextField(verbose_name='Descripción')),
                ('description_html', models.TextField(blank=True, editable=False)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250, verbose_name='Título')),
                ('summary', models.TextField(blank=True, verbose_name='Resumen')),
                ('body', models.TextField(verbose_name='Contenido')),
                ('extend', models.TextField(blank=True, verbose_name='Extendido')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('summary_html', models.TextField(blank=True, editable=False)),
                ('body_html', models.TextField(blank=True, editable=False)),
                ('extend_html', models.TextField(blank=True, editable=False)),
                ('enable_comments', models.BooleanField(default=True)),
                ('cover', models.URLField(blank=True)),
                ('slug', models.SlugField(unique_for_date='pub_date')),
                ('status', models.IntegerField(choices=[(1, 'Live'), (2, 'Draft'), (3, 'Hidden')], default=1)),
                ('featured', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
                'ordering': ['-entry__id', '-pub_date'],
                'get_latest_by': 'pub_date',
            },
        ),
        migrations.AlterUniqueTogether(
            name='entry',
            unique_together=set([('slug', 'pub_date')]),
        ),
    ]
