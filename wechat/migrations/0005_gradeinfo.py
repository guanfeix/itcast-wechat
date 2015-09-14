# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0004_studentinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.IntegerField()),
                ('stuName', models.ForeignKey(to='wechat.StudentInfo')),
                ('syllaID', models.ForeignKey(to='wechat.SyllabusInfo')),
            ],
        ),
    ]
