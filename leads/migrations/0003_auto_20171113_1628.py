# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-13 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20171109_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinings',
            name='aadhar_number',
            field=models.CharField(help_text='Enter your 12 digits Aadhar Number', max_length=150),
        ),
    ]
