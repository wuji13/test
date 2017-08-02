# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class article(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(null=True)

#管理后台数据显示title，2.7用def __unicode__(self):

    def __str__(self):
        return self.title
