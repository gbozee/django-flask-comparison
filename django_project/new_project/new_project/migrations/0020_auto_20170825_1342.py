# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_project', '0019_auto_20170823_0809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_pix',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='sentreport',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='sentreport',
            name='general_findings',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='sentreport',
            name='next_appointment',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='sentreport',
            name='presenting_complaints',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='sentreport',
            name='service_time',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='sentreport',
            name='treatment_plan',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='sentreport',
            name='vaccine_batchnumber',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='sentreport',
            name='vaccine_expirydate',
            field=models.DateField(blank=True),
        ),
    ]