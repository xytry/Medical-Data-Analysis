# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-31 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import patients.validators


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0011_auto_20180304_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsinfo',
            name='initial_primary_doctor',
            field=models.IntegerField(blank=True, help_text='1=HO/MO,2=Locum/GP,3=Registrar', null=True),
        ),
        migrations.AddField(
            model_name='patientsinfo',
            name='initial_shift',
            field=models.IntegerField(blank=True, help_text='1=AM,2=PM,3=Night', null=True),
        ),
        migrations.AlterField(
            model_name='patientsinfo',
            name='gender',
            field=models.IntegerField(blank=True, default='0', help_text='0=Male,1=Female', null=True, validators=[patients.validators.validate_gender]),
        ),
    ]