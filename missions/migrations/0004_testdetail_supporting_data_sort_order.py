# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-15 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0003_auto_event-id'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdetail',
            name='supporting_data_sort_order',
            field=models.TextField(blank=True, default=b'[]'),
        ),
    ]
