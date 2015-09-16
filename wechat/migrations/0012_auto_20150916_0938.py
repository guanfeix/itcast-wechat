# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0011_auto_20150916_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradeinfo',
            name='stuName',
        ),
        migrations.AddField(
            model_name='gradeinfo',
            name='stuID',
            field=models.ForeignKey(related_name='district_stu', default='', to='wechat.StudentInfo'),
            preserve_default=False,
        ),
    ]
