# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-27 00:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180326_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='response_post_id',
        ),
    ]