# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_blog_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='none', max_length=100, unique=True, verbose_name='slug'),
        ),
    ]