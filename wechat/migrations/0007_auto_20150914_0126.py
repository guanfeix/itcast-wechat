# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0006_academyinfo_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academyinfo',
            old_name='acodemyIntro',
            new_name='academyIntro',
        ),
        migrations.AddField(
            model_name='academyinfo',
            name='academyImage',
            field=models.ImageField(default='', upload_to=b'upload'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='academyinfo',
            name='imageAddress',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
    ]
