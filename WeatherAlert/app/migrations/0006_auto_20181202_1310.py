# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-02 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20181201_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofile',
            name='acknowledgment',
            field=models.BooleanField(default=False),
        ),
    ]
