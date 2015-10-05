# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0023_auto_20151003_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='inClass',
        ),
        migrations.AlterField(
            model_name='gradeinfo',
            name='stuID',
            field=models.ForeignKey(to='wechat.UserProfile'),
        ),
        migrations.DeleteModel(
            name='StudentInfo',
        ),
    ]
