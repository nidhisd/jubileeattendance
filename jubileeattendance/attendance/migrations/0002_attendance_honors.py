# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-25 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_marked', models.DateField()),
                ('am_pm', models.CharField(max_length=2)),
                ('timestamp', models.DateTimeField()),
                ('participant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='Honors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('participant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Participant')),
            ],
        ),
    ]