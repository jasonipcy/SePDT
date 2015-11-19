# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time_record',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='time_record',
            name='start_date',
        ),
        migrations.AddField(
            model_name='time_record',
            name='end_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='time_record',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
