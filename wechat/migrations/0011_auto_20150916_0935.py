# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0010_auto_20150915_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradeinfo',
            name='syllaID',
            field=models.ForeignKey(related_name='district_syll', to='wechat.SyllabusInfo'),
        ),
    ]
