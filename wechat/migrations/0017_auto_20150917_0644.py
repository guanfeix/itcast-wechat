# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0016_testansinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testansinfo',
            old_name='topicID',
            new_name='testInfoId',
        ),
    ]
