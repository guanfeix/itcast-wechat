# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0014_auto_20150916_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='Idcard',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='qq',
        ),
    ]
