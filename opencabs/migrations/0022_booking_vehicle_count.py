# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-28 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0021_auto_20180224_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='vehicle_count',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]
