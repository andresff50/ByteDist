# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-21 03:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mvideo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news_video',
            name='image1',
        ),
    ]