# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requirements', '__first__'),
        ('academia', '0004_auto_20150425_0549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=1020)),
                ('type', models.CharField(max_length=10)),
                ('college', models.ForeignKey(to='academia.College')),
                ('major', models.ManyToManyField(to='requirements.Requirement', related_name='required_for_major')),
                ('preMajor', models.ManyToManyField(to='requirements.Requirement', related_name='required_for_premajor')),
            ],
        ),
    ]
