# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0006_auto_20171214_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentaccount',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]