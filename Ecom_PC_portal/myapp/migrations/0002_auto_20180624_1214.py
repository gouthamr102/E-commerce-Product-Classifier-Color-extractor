# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-24 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=b'documents/codiecon/'),
        ),
    ]
