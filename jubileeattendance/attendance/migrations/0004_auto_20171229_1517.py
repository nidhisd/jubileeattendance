# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-29 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20171228_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date_marked',
            field=models.DateTimeField(),
        ),
    ]
