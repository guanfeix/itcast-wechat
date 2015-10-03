# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0019_auto_20150917_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testansinfo',
            name='rightOption1',
        ),
        migrations.RemoveField(
            model_name='testansinfo',
            name='rightOption2',
        ),
        migrations.AddField(
            model_name='testansinfo',
            name='rightOption',
            field=models.BooleanField(default=False),
        ),
    ]
