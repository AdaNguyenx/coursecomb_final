# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-04 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0032_auto_20180504_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='evals',
            field=models.TextField(),
        ),
    ]