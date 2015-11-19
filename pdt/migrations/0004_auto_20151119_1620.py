# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0003_auto_20151118_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginuser',
            name='user',
        ),
        migrations.AlterField(
            model_name='code',
            name='manager_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='defect',
            name='developer_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='developer_id',
            field=models.ManyToManyField(related_name='User_Project_Developer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='manager_id',
            field=models.ForeignKey(related_name='User_Project_Manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='time_record',
            name='developer_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='LoginUser',
        ),
    ]
