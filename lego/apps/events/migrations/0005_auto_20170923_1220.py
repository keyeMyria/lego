# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20170921_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_ready',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pool',
            name='counter',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]