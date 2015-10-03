# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0017_auto_20150917_0644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testinfo',
            name='result',
        ),
        migrations.AddField(
            model_name='testansinfo',
            name='right',
            field=models.BooleanField(default=False),
        ),
    ]
