# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sutasshuapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date added'),
        ),
    ]
