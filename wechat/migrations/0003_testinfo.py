# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0002_syllabusinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.TextField()),
                ('result', models.TextField()),
                ('syllaID', models.ForeignKey(to='wechat.SyllabusInfo')),
            ],
        ),
    ]
