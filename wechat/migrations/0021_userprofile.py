# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wechat', '0020_auto_20150917_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(unique=True, max_length=100)),
                ('isRegister', models.BooleanField(default=False)),
                ('nickName', models.CharField(max_length=30)),
                ('stuSex', models.IntegerField(default=True)),
                ('stuName', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=20)),
                ('photoAddr', models.URLField()),
                ('createTime', models.DateField()),
                ('lastTime', models.DateField()),
                ('inClass', models.ForeignKey(to='wechat.ClassInfo')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
