# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0013_auto_20150916_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradeinfo',
            name='grade',
            field=models.CharField(max_length=10),
        ),
    ]
