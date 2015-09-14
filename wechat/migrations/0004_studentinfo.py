# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0003_testinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(unique=True, max_length=100)),
                ('isRegister', models.BooleanField(default=False)),
                ('nickName', models.CharField(max_length=30)),
                ('stuSex', models.BooleanField(default=True)),
                ('stuName', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=20)),
                ('qq', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('Idcard', models.CharField(max_length=30)),
                ('photoAddr', models.URLField()),
                ('createTime', models.DateField()),
                ('lastTime', models.DateField()),
                ('inClass', models.ForeignKey(to='wechat.ClassInfo')),
            ],
        ),
    ]
