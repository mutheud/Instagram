# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-17 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20181217_0824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='Image_caption',
            new_name='image_caption',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='Image_name',
            new_name='image_name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='Likes',
            new_name='likes',
        ),
    ]
