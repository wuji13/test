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
	print(article_id)
	art = models.article.objects.get(pk=article_id)
	return  render(request,'blog/article_page.html',{'b':art})

def edit_page(request,article_id):
	if str(article_id)=='0':
		return render(request, 'blog/edit_page.html')
	art = models.article.objects.get(pk=article_id)
	return render(request,'blog/edit_page.html',{'c':art})

def edit_submit(request):
	title = request.POST.get('title', 'TITLE')
	content = request.POST.get('content', 'content')
	article_id = request.POST.get('id', 'id')
	if article_id=='0':
	  models.article.objects.create(title=title,content=content)
	  articles = models.article.objects.all
	  return render(request, 'blog/index.html', {'a': articles})
	else:
		a=models.article.objects.get(pk=article_id)
		a.title=title
		a.content=content
		a.save()
		return render(request, 'blog/article_page.html', {'b':a})







