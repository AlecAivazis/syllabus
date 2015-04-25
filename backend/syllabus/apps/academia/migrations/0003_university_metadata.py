# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '__first__'),
        ('academia', '0002_remove_university_metadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='metadata',
            field=models.ManyToManyField(to='metadata.Metadata'),
        ),
    ]
