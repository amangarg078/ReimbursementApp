# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-20 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='reimbursement',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
