# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-31 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_tags_response_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='response_post',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
