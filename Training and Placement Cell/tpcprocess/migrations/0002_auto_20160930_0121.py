# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-29 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpcprocess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.TextField(max_length=100),
        ),
    ]
