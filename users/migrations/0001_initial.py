# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 15:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_auth', models.CharField(max_length=1024)),
                ('google_auth', models.CharField(max_length=1024)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='app_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
