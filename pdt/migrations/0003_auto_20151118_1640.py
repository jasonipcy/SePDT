# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0002_auto_20151118_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_record',
            name='end_time',
            field=models.DateTimeField(),
        ),
    ]
