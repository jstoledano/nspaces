# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-03 05:06
from __future__ import unicode_literals

from django.db import migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_merge_20170802_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
