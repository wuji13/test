# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class article(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(null=True)

