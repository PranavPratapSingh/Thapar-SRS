# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-14 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRS', '0008_srs_feedbackscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='batch',
            field=models.CharField(default='2co21', max_length=5),
            preserve_default=False,
        ),
    ]