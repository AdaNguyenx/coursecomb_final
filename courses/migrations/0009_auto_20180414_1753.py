# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20180412_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filtered', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='course_combo',
        ),
        migrations.AddField(
            model_name='combination',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='combinations', to='courses.Profile'),
        ),
    ]