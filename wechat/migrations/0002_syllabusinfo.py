# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyllabusInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lessonName', models.CharField(max_length=300)),
                ('lessonContent', models.TextField()),
                ('timeOut', models.IntegerField()),
                ('academyID', models.ForeignKey(to='wechat.AcademyInfo')),
            ],
        ),
    ]
