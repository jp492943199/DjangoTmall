# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-07 22:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salers', '0002_tmallshop_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tmallshop',
            old_name='BusinessLicense',
            new_name='businessLicense',
        ),
    ]
