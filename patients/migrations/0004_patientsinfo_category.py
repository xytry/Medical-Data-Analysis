# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-03 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20180303_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsinfo',
            name='category',
            field=models.CharField(blank=True, default='Male', max_length=10, null=True),
        ),
    ]