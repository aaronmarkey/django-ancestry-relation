# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_ancestry_relation', '0002_auto_20170828_2007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testnode',
            options={'managed': False},
        ),
    ]