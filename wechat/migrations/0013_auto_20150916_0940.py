# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0012_auto_20150916_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradeinfo',
            name='stuID',
            field=models.ForeignKey(to='wechat.StudentInfo'),
        ),
        migrations.AlterField(
            model_name='gradeinfo',
            name='syllaID',
            field=models.ForeignKey(to='wechat.SyllabusInfo'),
        ),
    ]
