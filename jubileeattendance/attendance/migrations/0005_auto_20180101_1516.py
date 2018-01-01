# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-01 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20171229_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='honors',
            name='participant_id',
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='participant_id',
            new_name='participant',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='email_id',
        ),
        migrations.AddField(
            model_name='participant',
            name='grade',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Honors',
        ),
    ]