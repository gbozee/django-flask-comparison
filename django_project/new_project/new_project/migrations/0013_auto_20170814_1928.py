# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 19:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new_project', '0012_auto_20170814_0520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthservice',
            name='providers',
        ),
        migrations.AddField(
            model_name='healthservice',
            name='provider_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='new_project.Provider'),
        ),
        migrations.RemoveField(
            model_name='provider',
            name='likes',
        ),
        migrations.AddField(
            model_name='provider',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='provider_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]