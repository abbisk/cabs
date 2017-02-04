# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0008_auto_20170204_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='opencabs.Driver'),
        ),
        migrations.AddField(
            model_name='booking',
            name='extrainfo',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='booking',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='opencabs.Vehicle'),
        ),
    ]