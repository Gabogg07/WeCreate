# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIGPAE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='anio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='codigo',
            field=models.CharField(default='', max_length=10),
        ),
    ]