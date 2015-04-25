# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import syllabus.fields


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0003_university_metadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=1020)),
                ('full_name', models.CharField(max_length=1020)),
                ('units', models.IntegerField()),
                ('description', models.CharField(max_length=1020)),
                ('number', models.IntegerField()),
                ('interest', models.ForeignKey(related_name='course_profiles', to='academia.Interest')),
            ],
        ),
        migrations.RemoveField(
            model_name='college',
            name='departments',
        ),
        migrations.RemoveField(
            model_name='department',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='university',
            name='metadata',
        ),
        migrations.AddField(
            model_name='department',
            name='college',
            field=models.ForeignKey(to='academia.College', related_name='departments', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='min_grade_to_pass',
            field=syllabus.fields.GradeField(decimal_places=2, max_digits=4, default=0),
            preserve_default=False,
        ),
    ]
