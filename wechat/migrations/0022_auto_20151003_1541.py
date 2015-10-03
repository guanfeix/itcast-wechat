# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0021_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='fromUser',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='isRegister',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='openid',
        ),
    ]
