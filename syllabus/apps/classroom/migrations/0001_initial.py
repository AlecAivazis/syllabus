# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=1020)),
                ('description', models.TextField(max_length=5000)),
                ('date', models.DateField()),
                ('start', models.TimeField(blank=True)),
                ('end', models.TimeField(blank=True)),
                ('category', models.CharField(blank=True, choices=[('assignment', 'assignment'), ('test', 'test'), ('lecture', 'lecture'), ('meeting', 'meeting')], max_length=1020)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
