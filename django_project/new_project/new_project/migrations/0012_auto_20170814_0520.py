# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_project', '0011_auto_20170813_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentreport',
            name='report_type',
            field=models.CharField(choices=[('CO', 'Consultation'), ('VA', 'Vaccine'), ('MI', 'Microbiology'), ('OT', 'Other Reports')], max_length=50),
        ),
    ]
