# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-14 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universities',
            name='id',
        ),
        migrations.AlterField(
            model_name='universities',
            name='uniCode',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]