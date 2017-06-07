# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import article

#在admin中注册models
admin.site.register(article)
