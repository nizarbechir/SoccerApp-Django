# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccerApp', '0004_auto_20170329_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
