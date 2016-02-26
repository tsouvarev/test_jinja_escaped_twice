# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('status', models.IntegerField(choices=[(0, 'Unpublished'), (1, 'Published')])),
            ],
        ),
    ]
