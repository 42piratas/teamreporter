# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('teamreporter', '0008_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='id',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='slug',
        ),
        migrations.AddField(
            model_name='survey',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
