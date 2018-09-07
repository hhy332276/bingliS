# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Account(models.Model):
    account = models.CharField(max_length=32,verbose_name='用户')
    passwd = models.CharField(max_length=32,verbose_name='密码')
    user_name = models.CharField(max_length=32,verbose_name='用户名')
    state = models.IntegerField(default=0,verbose_name='状态')
    create_time = models.DateTimeField(default=datetime.now,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    class Meta:
        verbose_name_plural = verbose_name = '用户信息'

