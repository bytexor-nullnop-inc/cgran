# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Outoftreemodule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('tags', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('repo', models.URLField()),
                ('added_date', models.DateField()),
            ],
        ),
    ]
