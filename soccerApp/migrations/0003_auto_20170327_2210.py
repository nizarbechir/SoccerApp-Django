# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('soccerApp', '0002_auto_20170327_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='nbGoals1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='nbGoals2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='nbGoal',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='playedGames',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='totalPoint',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='totalVictories',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
