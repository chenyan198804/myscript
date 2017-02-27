# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_args'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=256, null=True)),
                ('create_data', models.DateTimeField(auto_now=True, error_messages={'invalid': '??????'})),
                ('update_data', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo_Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserType', models.CharField(choices=[('1', '普通用户'), ('2', '管理员'), ('3', '超级管理员')], max_length=2)),
            ],
        ),
    ]
