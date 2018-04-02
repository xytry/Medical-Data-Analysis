# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-03 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_patientsinfo_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsinfo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='patientsinfo',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
