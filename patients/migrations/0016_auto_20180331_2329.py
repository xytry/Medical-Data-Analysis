# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-31 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0015_auto_20180331_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsinfo',
            name='abdominal_pain',
            field=models.IntegerField(blank=True, default='0', help_text='0=No, 1=Yes', null=True),
        ),
        migrations.AddField(
            model_name='patientsinfo',
            name='asthma',
            field=models.IntegerField(blank=True, default='0', help_text='0=No, 1=Yes', null=True),
        ),
        migrations.AddField(
            model_name='patientsinfo',
            name='cerebral_palsy',
            field=models.IntegerField(blank=True, default='0', help_text='0=No, 1=Yes', null=True),
        ),
        migrations.AddField(
            model_name='patientsinfo',
            name='diarrhea',
            field=models.IntegerField(blank=True, default='0', help_text='0=No, 1=Yes', null=True),
        ),
        migrations.AddField(
            model_name='patientsinfo',
            name='fever',
            field=models.IntegerField(blank=True, default='0', help_text='0=No, 1=Yes', null=True),
        ),
        migrations.AddField(
            model_name='patientsinfo',
            name='giddiness',
            field=models.IntegerField(blank=True, default='0', help_text='0=No, 1=Yes', null=True),
        ),
        migrations.AddField(
            model_name='patientsinfo',
            name='low_back_pain',
            field=models.IntegerField(blank=True, default='0', help_text='0=No, 1=Yes', null=True),
        ),
        migrations.AddField(
            model_name='patientsinfo',
            name='nausea_vomiting',
            field=models.IntegerField(blank=True, default='0', help_text='0=No, 1=Yes', null=True),
        ),
        migrations.AddField(
            model_name='patientsinfo',
            name='renal_colic',
            field=models.IntegerField(blank=True, default='0', help_text='0=No, 1=Yes', null=True),
        ),
        migrations.AddField(
            model_name='patientsinfo',
            name='trauma',
            field=models.IntegerField(blank=True, default='0', help_text='0=No, 1=Yes', null=True),
        ),
        migrations.AddField(
            model_name='patientsinfo',
            name='upper_respiratory_tract_infections',
            field=models.IntegerField(blank=True, default='0', help_text='0=No, 1=Yes', null=True),
        ),
    ]
