# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=150)),
                ('order_date', models.DateTimeField(verbose_name='date published')),
                ('state', models.IntegerField(default=0)),
            ],
        ),
    ]
