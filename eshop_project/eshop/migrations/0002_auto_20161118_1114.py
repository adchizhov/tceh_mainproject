# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 08:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phoneproduct',
            old_name='name',
            new_name='phone_model',
        ),
        migrations.RemoveField(
            model_name='phoneproduct',
            name='category',
        ),
    ]