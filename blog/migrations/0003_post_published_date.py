# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170821_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]