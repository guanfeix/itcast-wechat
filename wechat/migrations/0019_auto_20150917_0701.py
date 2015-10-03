# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0018_auto_20150917_0658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testansinfo',
            old_name='right',
            new_name='rightOption1',
        ),
        migrations.AddField(
            model_name='testansinfo',
            name='rightOption2',
            field=models.BooleanField(default=False),
        ),
    ]
