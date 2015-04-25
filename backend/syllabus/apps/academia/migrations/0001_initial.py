# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=1020)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=1020)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=1020)),
                ('abbrv', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=1020)),
                ('metadata', models.ManyToManyField(to='metadata.Metadata')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='department',
            name='interests',
            field=models.ManyToManyField(related_name='department', to='academia.Interest'),
        ),
        migrations.AddField(
            model_name='college',
            name='departments',
            field=models.ManyToManyField(related_name='college', to='academia.Department', blank=True),
        ),
        migrations.AddField(
            model_name='college',
            name='university',
            field=models.ForeignKey(related_name='colleges', to='academia.University'),
        ),
    ]
