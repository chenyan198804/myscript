# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Gender', models.BooleanField(default=False)),
                ('Age', models.IntegerField(default=19)),
                ('Memo', models.TextField(default='xxxx')),
                ('Creatdate', models.DateTimeField(default='2014-12-12 12:12')),
            ],
        ),
    ]
