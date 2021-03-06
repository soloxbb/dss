# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-14 07:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualAddInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manualinfo_text', models.CharField(max_length=200)),
                ('operatorname', models.CharField(max_length=20)),
                ('consequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.Consequence')),
            ],
        ),
        migrations.CreateModel(
            name='ManualComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manualcomments_text', models.CharField(max_length=200)),
                ('operatorname', models.CharField(max_length=20)),
                ('consequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.Consequence')),
            ],
        ),
    ]
