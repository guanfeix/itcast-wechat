# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademyInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academyName', models.CharField(unique=True, max_length=100)),
                ('academyPre', models.CharField(max_length=30)),
                ('acodemyIntro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('className', models.CharField(max_length=100)),
                ('classBegDate', models.DateField()),
                ('classCharge', models.CharField(max_length=30)),
                ('academyID', models.ForeignKey(to='wechat.AcademyInfo')),
            ],
        ),
    ]
