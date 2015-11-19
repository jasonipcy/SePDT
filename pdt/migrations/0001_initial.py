# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('code_size', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('defect_name', models.CharField(max_length=40)),
                ('defect_type', models.CharField(max_length=3, choices=[('req', 'Requirement'), ('des', 'Design'), ('imp', 'Implementation'), ('bad', 'Bad_fix')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Iteration',
            fields=[
                ('iteration_id', models.AutoField(primary_key=True, serialize=False)),
                ('iteration_version', models.IntegerField()),
                ('iteration_start_date', models.DateField()),
                ('iteration_end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('user_type', models.CharField(max_length=3, choices=[('dev', 'Developer'), ('man', 'Manager')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('phase_id', models.AutoField(primary_key=True, serialize=False)),
                ('phase_name', models.CharField(max_length=3, choices=[('inc', 'Inception'), ('ela', 'Elaboration'), ('con', 'Construction'), ('tra', 'Transition')])),
                ('phase_start_date', models.DateField()),
                ('phase_end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=80)),
                ('project_description', models.TextField(blank=True, null=True)),
                ('project_start_date', models.DateField()),
                ('project_end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('developer_id', models.ManyToManyField(to='pdt.LoginUser', related_name='User_Project_Developer')),
                ('manager_id', models.ForeignKey(to='pdt.LoginUser', related_name='User_Project_Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Time_Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('activity', models.CharField(max_length=3, choices=[('dev', 'Development'), ('def', 'Defects_removal')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_time', models.DateTimeField()),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('developer_id', models.ForeignKey(to='pdt.LoginUser')),
                ('iteration_id', models.ForeignKey(to='pdt.Iteration')),
            ],
        ),
        migrations.AddField(
            model_name='phase',
            name='project_id',
            field=models.ForeignKey(to='pdt.Project'),
        ),
        migrations.AddField(
            model_name='iteration',
            name='phase_id',
            field=models.ForeignKey(to='pdt.Phase'),
        ),
        migrations.AddField(
            model_name='defect',
            name='current_iteration_id',
            field=models.ForeignKey(to='pdt.Iteration', related_name='Iteration_Defect_currect'),
        ),
        migrations.AddField(
            model_name='defect',
            name='defect_iteration_id',
            field=models.ForeignKey(to='pdt.Iteration', related_name='Iteration_Defect_defect'),
        ),
        migrations.AddField(
            model_name='defect',
            name='developer_id',
            field=models.ForeignKey(to='pdt.LoginUser'),
        ),
        migrations.AddField(
            model_name='code',
            name='iteration_id',
            field=models.ForeignKey(to='pdt.Iteration'),
        ),
        migrations.AddField(
            model_name='code',
            name='manager_id',
            field=models.ForeignKey(to='pdt.LoginUser'),
        ),
    ]
