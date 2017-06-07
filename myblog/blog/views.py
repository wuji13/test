# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):
	# 返回全部对象，.get(pk=?)获取某个对象
	articles = models.article.objects.all
	return  render(request,'blog/index.html',{'a':articles})

def article(request,article_id):
	art = models.article.objects.get(pk=article_id)
	return  render(request,'blog/article_page.html',{'b':art})

def edit(request):
	return  render(request,'blog/edit_page.html')

def edit_submit(request):
	title=request.POST.get('title','TITLE')
	content=request.POST.get('content','content')
	models.article.objects.create(title=title,content=content)
	articles = models.article.objects.all
	return render(request, 'blog/index.html', {'a': articles})



