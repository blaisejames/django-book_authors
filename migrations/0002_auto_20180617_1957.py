# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-17 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
