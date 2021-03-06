# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-13 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consequence_text', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Likelihood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likelihood_text', models.CharField(max_length=20)),
                ('consequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.Consequence')),
            ],
        ),
        migrations.CreateModel(
            name='MissingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missinginfo_text', models.CharField(max_length=200)),
                ('consequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.Consequence')),
            ],
        ),
        migrations.CreateModel(
            name='Severity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity_text', models.CharField(max_length=20)),
                ('consequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.Consequence')),
            ],
        ),
    ]
