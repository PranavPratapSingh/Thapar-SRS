# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-14 08:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SRS', '0002_auto_20180414_1404'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='universities',
            new_name='university',
        ),
    ]
