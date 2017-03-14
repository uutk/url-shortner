# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-14 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import shortner.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0004_auto_20170314_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chotaurl',
            name='url',
            field=models.CharField(max_length=220, unique=True, validators=[shortner.validators.validate_url, shortner.validators.validate_dot_com]),
        ),
    ]