# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0009_classinfo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='stuSex',
            field=models.IntegerField(default=True),
        ),
    ]
