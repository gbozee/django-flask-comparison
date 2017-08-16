# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_project', '0006_auto_20170809_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='providerprofile',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='providerprofile',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ambulreport',
            name='pickup_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='measuredtest',
            name='service_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='myhealth',
            name='service_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='orderedservice',
            name='preferred_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='requests',
            name='request_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sentreport',
            name='service_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sentreport',
            name='vaccine_expirydate',
            field=models.DateField(),
        ),
    ]