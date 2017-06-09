# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import article


class articleAdmin(admin.ModelAdmin):
    list_display=('id','title','content')
    #过滤器，起筛选作用
    list_filter=('id',)
#在admin中注册models
admin.site.register(article,articleAdmin)
