# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0015_auto_20150916_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAnsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option', models.CharField(max_length=300)),
                ('topicID', models.ForeignKey(to='wechat.TestInfo')),
            ],
        ),
    ]
