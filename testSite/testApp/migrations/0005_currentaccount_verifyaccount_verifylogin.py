# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0004_bussiness_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('newsPageLikeOrDislike', models.BooleanField(default=False)),
                ('sportPageLikeOrDislike', models.BooleanField(default=False)),
                ('bizPageLikeOrDislike', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VerifyAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isNewAccount', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VerifyLogIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernameExists', models.CharField(max_length=100)),
                ('passwordExists', models.CharField(max_length=100)),
            ],
        ),
    ]
