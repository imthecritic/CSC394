# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-17 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161016_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='cs_class',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='is_class',
        ),
        migrations.AddField(
            model_name='degreerequirements',
            name='required',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
