# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0007_auto_20150914_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academyinfo',
            name='imageAddress',
        ),
    ]
