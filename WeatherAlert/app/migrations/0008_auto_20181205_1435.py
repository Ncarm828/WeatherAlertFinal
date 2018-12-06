# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 19:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181205_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='usersprofile',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
