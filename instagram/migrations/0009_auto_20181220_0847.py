# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 08:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0008_auto_20181220_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='Image_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
